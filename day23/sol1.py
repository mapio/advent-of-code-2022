import fileinput
from operator import itemgetter
from collections import defaultdict 

def north(r, c):
  return { 
    (r - 1, c - 1),
    (r - 1, c    ),
    (r - 1, c + 1)
  }, (r - 1, c)

def east(r, c):
  return { 
    (r + 1, c + 1),
    (r    , c + 1),
    (r - 1, c + 1)
  }, (r, c + 1)

def south(r, c):
  return { 
    (r + 1, c - 1),
    (r + 1, c    ),
    (r + 1, c + 1)
  }, (r + 1, c)

def west(r, c):
  return { 
    (r + 1, c - 1),
    (r    , c - 1),
    (r - 1, c - 1)
  }, (r, c - 1)

def around(r, c):
  return north(r, c)[0] | east(r, c)[0] | south(r, c)[0] | west(r, c)[0]

ELVES = set()
for r, line in enumerate(fileinput.input()):
  for c, v in enumerate(line.strip()):
    if v == '#': ELVES.add((r, c))

PROPOSALS = [north, south, east, west]
p = 0

def round(curelves, p):
  proposal = defaultdict(list)
  for elf in curelves:
    if not (around(*elf) & curelves):
      proposal[elf].append(elf)
    else:
      for i in range(4):
        pos, elfp = PROPOSALS[(p + i) % 4](*elf)
        if not (curelves & pos):
          proposal[elfp].append(elf)
          break
  nextelves = set()
  for elfp, elves in proposal.items():
    if len(elves) > 1: nextelves |= set(elves)
    else: nextelves.add(elfp)
  return nextelves

def pe(elves):
  mr, Mr = min(map(itemgetter(0), elves)), max(map(itemgetter(0), elves))
  mc, Mc = min(map(itemgetter(1), elves)), max(map(itemgetter(1), elves))
  print('-' * ((Mr - mr) + 5))
  for r in range(mr - 3, Mr + 4):
    for c in range(mc - 3, Mc + 4):
      print('#' if (r, c) in elves else '.', end = '')
    print()


elves = ELVES
p = 0
pe(elves)
while True:
  nextelves = round(elves, p)
  pe(nextelves)
  print(nextelves)
  if nextelves == elves: break
  p = (p + 1) % 4
  elves = nextelves