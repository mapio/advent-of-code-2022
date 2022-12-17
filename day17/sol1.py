import fileinput
from itertools import cycle

def maxy(s):
  return max(y for _, y in s)

def maxx(s):
  return max(x for x, _ in s)

def minx(s):
  return min(x for x, _ in s)

class Tile:

  def __init__(self, pts):
    self.pts = pts
    self.minx = minx(pts)
    self.maxx = maxx(pts)

  def T(self, tx, ty):
    return Tile({(x + tx, y + ty) for x, y in self.pts})

  def R(self):
    r = self.T(1, 0)
    return r if r.maxx < 7 else self

  def L(self):
    l = self.T(-1, 0)
    return l if l.minx >= 0 else self

  def D(self):
    return self.T(0, -1)

  def __and__(self, o):
    return self.pts & o
  def __rand__(self, o):
    return self.pts & o

  def __or__(self, o):
    return self.pts | o
  def __ror__(self, o):
    return self.pts | o

  def __repr__(self):
    return repr(self.pts)


def pset(s):
  mx, my = maxx(s), maxy(s)
  for y in range(my, 0, -1):
    print('|', end = '')
    for x in range(0, mx + 1):
      print('#' if (x, y) in s else '.', end = '')
    print('|')
  print('+-------+')

TILES = [
  Tile({(0, 0), (1, 0), (2, 0), (3, 0)}),
  Tile({(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}),
  Tile({(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}),
  Tile({(0, 0), (0, 1), (0, 2), (0, 3)}),
  Tile({(0, 0), (0, 1), (1, 0), (1, 1)})
]

FIELD = {(x, 0) for x in range(7)}

CMDS = iter(next(fileinput.input()).strip())

itt = iter(cycle(TILES))
y = maxy(FIELD) + 4
x = 2
t = next(itt).T(x, y)
fallen = 0
for c in cycle(CMDS):
  if c == '>': 
    tp = t.R()
    t = t if tp & FIELD else tp
  elif c == '<': 
    tp = t.L()
    t = t if tp & FIELD else tp
  tp = t.D()
  if tp & FIELD:
    FIELD |= t
    fallen += 1
    print(maxy(FIELD))
    if fallen == 10_000:
      break
    t = next(itt).T(2, maxy(FIELD) + 4)
    #pset(FIELD)
  else:
    t = tp
    #pset(FIELD | t)
 
#pset(FIELD)
