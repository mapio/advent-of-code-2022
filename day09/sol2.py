import fileinput

class Node:
  def __init__(self, name, nxt = None):
    self.x = 0
    self.y = 0
    self.name = name
    self.nxt = nxt
  def move(self, dir):
    if dir == 'U':
      self.y +=1
    elif dir == 'D':
      self.y -=1
    elif dir == 'L':
      self.x -= 1
    elif dir == 'R':
      self.x += 1
    if self.nxt: self.nxt.chase(self)
    _print(self, 30)
  def moves(self, dir, steps):
    for _ in range(steps): self.move(dir)
  def chase(self, prev):
    #print(f'{self.name}{(self.x, self.y)} chase {prev.name}{(prev.x, prev.y)}', end = '')
    if self.x == prev.x and self.y == prev.y: 
      #print()
      return
    if self.x == prev.x and abs(self.y - prev.y) == 2:
      self.y -= (self.y - prev.y) // 2
    elif self.y == prev.y and abs(self.x - prev.x) == 2:
      self.x -= (self.x - prev.x) // 2
    else:
      dx = self.x - prev.x
      dy = self.y - prev.y
      if abs(dx) == 1 and abs(dy) == 2:
        self.x -= dx
        self.y -= dy // 2
      elif abs(dx) == 2 and abs(dy) == 1:
        self.x -= dx // 2
        self.y -= dy
      elif abs(dx) == abs(dy) == 2:
        self.x -= dx // 2
        self.y -= dy // 2
    #print(f'-> {(self.x, self.y)}')
    if self.nxt: self.nxt.chase(self)
    else: POS.add((self.x, self.y))
  def __repr__(self):
    return f'{self.name}({self.x}, {self.y}) {("-> " + str(self.nxt)) if self.nxt else ""}'

POS = set()
h = None
for i in range(9, -1, -1):
  h = Node(i, h)

def _print(h, n):
  return
  M = [['.'] * n for _ in range(n)]
  p = h
  while p:
    name = 'H' if p.name == 0 else str(p.name)
    old = M[n//2 - p.y][p.x + n//2]
    if old == '.' or old > name: 
      M[n//2 - p.y][p.x + n//2] = name
    p = p.nxt
  print('\n'.join(map(''.join, M)))
  print('=' * n)

for line in fileinput.input():
  d, n = line.strip().split()
  h.moves(d, int(n))

print(len(POS))
