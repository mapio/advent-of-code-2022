import fileinput
import re
import operator

op2l = {
  '+': operator.add,
  '*': operator.mul,
}

class Monkey:

  MONKEYS = dict()

  MOD = 1

  PATTERN = re.compile(r"""Monkey (?P<num>\d+):
\s+Starting items: (?P<items>((\d+)(, )?)+)
\s+Operation: new = old (?P<op>.) (?P<val>\w+)
\s+Test: divisible by (?P<by>\d+)
\s+If true: throw to monkey (?P<true>\d+)
\s+If false: throw to monkey (?P<false>\d+)""")
  
  def __init__(self, blk):
    param = Monkey.PATTERN.match(blk).groupdict()
    self.num = int(param['num'])
    self.op = param['op']
    self.val = 'old' if param['val'] == 'old' else int(param['val'])
    self.by = int(param['by'])
    self.true = int(param['true'])
    self.false = int(param['false'])
    self.activity = 0
    self.items = list(map(int, param['items'].split(',')))
    Monkey.MONKEYS[self.num] = self
    Monkey.MOD *= self.by 

  def append(self, item):
    self.items.append(item % Monkey.MOD)

  @classmethod
  def ROUND(cls):
    for m in sorted(cls.MONKEYS.keys()):
      cls.MONKEYS[m].round()

  @classmethod
  def ACTIVITIES(cls):
    return [m.activity for m in cls.MONKEYS.values()]

  @classmethod
  def BUSINESS(cls):
    return operator.mul(*sorted((m.activity for m in cls.MONKEYS.values()), reverse = True)[:2])

  def round(self):
    def _round(item):
      item = op2l[self.op](item, (item if self.val == 'old' else self.val)) 
      if item % self.by == 0:
        Monkey.MONKEYS[self.true].append(item)
      else:
        Monkey.MONKEYS[self.false].append(item)
    while self.items:
      self.activity +=1 
      _round(self.items.pop(0))

  def __repr__(self):
    return f'Monkey {self.num}: {self.items} ({self.activity})'

blk = ''
for line in fileinput.input():
  if line == '\n': 
    Monkey(blk)
    blk = ''
  else:
    blk += line
Monkey(blk)

for _ in range(10_000): Monkey.ROUND()
print(Monkey.BUSINESS())