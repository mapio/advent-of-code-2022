from dataclasses import dataclass, field
import fileinput
import numpy as np
import re
from math import sqrt 

##########

it = iter(fileinput.input())

M = []
N2 = 0
C = 0
for line in it:
  if not line.strip(): break
  line = list(line)[:-1]
  C = max(C, len(line))
  N2 += sum(1 for _ in line if _ != ' ')
  M.append(line)
N = int(sqrt(N2//6))
R = len(M) // N
C //= N

MOVES = next(it).strip()

##########

@dataclass
class Face:
  name: str = None
  M: list[list[int]] = field(default_factory=list[list[int]])
  O: list[list[int]] = field(default_factory=list[list[int]])
  north = None
  south = None
  east = None
  west = None

  def out(self, rc):
    r, c = rc
    if r < 0: return self.north
    if c >= N: return self.east
    if r >= N: return self.south
    if c < 0: return self.west
    return None

  def __repr__(self):
    return (self.name if self.name else '@') #+ str(self.M)

F = [[Face() for _ in range (C)] for _ in range(R)]
for br in range(R):
  for r in range(N * br, N * (br + 1)):
    for cr in range(C):
      if (cr + 1) * N <= len(M[r]):
        frr = M[r][cr * N : (cr + 1) * N]
        if '.' in frr or '#' in frr: 
          F[br][cr].M.append(frr)
          F[br][cr].O.append([(r, c) for c in range(cr * N, (cr + 1) * N)])
        else:
          F[br][cr] = None
      else:
        F[br][cr] = None

print('Faces: \n')

FM = dict()
face = 'A'
for r, row in enumerate(F):
  print('  ', end = '')
  for c, f in enumerate(row):
    if f:
      F[r][c].name = face
      FM[face] = f
      print(face, end = '')
      face = chr(ord(face) + 1)
    else:
      print('.', end = '')
  print()

##########

DIR = [
  np.array([ 0,  1]),
  np.array([ 1,  0]),
  np.array([ 0, -1]),
  np.array([-1,  0])
]

MDIR = ['>', 'v', '<', '^']

@dataclass
class PD:
  face: Face = None
  rc: np.array = np.array([0, 0])
  d: int = 0

  def val(self):
    return self.face.M[self.rc[0]][self.rc[1]]

  def orc(self):
    return self.face.O[self.rc[0]][self.rc[1]]

  def move(self):
    ppd = PD(self.face, self.rc + DIR[self.d], self.d)
    out = self.face.out(ppd.rc)
    if out: return out(ppd)
    return ppd

  def __eq__(self, other):
    return self.face == other.face and all(self.rc == other.rc) and self.d == other.d

  def __init__(self, face, rc, d):
    self.face = FM[face] if isinstance(face, str) else face
    self.rc = np.array(rc)
    self.d = MDIR.index(d) if isinstance(d, str) else d

def setmaps():
  idm = lambda pd: pd
  inv = lambda rc : N - 1 - rc
  r = lambda pd: pd.rc[0]
  c = lambda pd: pd.rc[1]
  invr = lambda pd: inv(r(pd))
  invc = lambda pd: inv(c(pd))
  f = lambda face: (lambda pd: PD(face, [pd.rc[0] % N, pd.rc[1] % N], pd.d))

  FM['A'].north = lambda pd: PD('F', [c(pd) ,0], '>')
  FM['A'].east  = f('B')
  FM['A'].south = f('C')
  FM['A'].west  = lambda pd: PD('D', [invr(pd), 0], '>')

  FM['B'].north = f('F')
  FM['B'].east  = lambda pd: PD('E', [invr(pd), N - 1], '<')
  FM['B'].south = lambda pd: PD('C', [c(pd), N - 1], '<')
  FM['B'].west  = f('A')

  FM['C'].north = f('A')
  FM['C'].east  = lambda pd: PD('B', [N - 1, r(pd)], '^')
  FM['C'].south = f('E')
  FM['C'].west  = lambda pd: PD('D', [0, r(pd)], 'v')

  FM['D'].north = lambda pd: PD('C', [c(pd), 0], '>')
  FM['D'].east  = f('E')
  FM['D'].south = f('F')
  FM['D'].west  = lambda pd: PD('A', [invr(pd), 0 ], '>')

  FM['E'].north = f('C')
  FM['E'].east  = lambda pd: PD('B', [invr(pd), N -1], '<')
  FM['E'].south = lambda pd: PD('F', [c(pd), N - 1], '<')
  FM['E'].west  = f('D')

  FM['F'].north = f('D')
  FM['F'].east  = lambda pd: PD('E', [N - 1, r(pd)], '^')
  FM['F'].south = lambda pd: PD('B', [0, c(pd)], 'v')
  FM['F'].west  = lambda pd: PD('A', [0, r(pd)], 'v')

setmaps()

if False:
  for d in range(4):
    print('Dir:', MDIR[d], end = ' ')
    for face in 'ABCDEF':
      print(face, end = '')
      errors = False
      for r in range(N):
        for c in range(N):
          pd0 = PD(face, [r, c], d)
          pd = pd0
          for _ in range(4 * N):
            pd = pd.move()
          if pd != pd0: errors = True
      print('!' if errors else ' ', end = ' ')
    print()

##########

def move(pd, dist):
  while dist > 0:
    opd = pd
    pd = pd.move()
    v = pd.val()
    if v == '.': dist -= 1
    elif v == '#': 
      print('bump')
      return opd
  return pd

face = FM['A']
pd = PD('A', [0, 0], '>')

for m in re.findall(r'\d+|R|L', MOVES):
  print(pd)
  if m == 'R':
    pd.d = (pd.d + 1) % 4
  elif m == 'L':
    pd.d = (pd.d - 1) % 4
  else:
    pd = move(pd, int(m))

r, c = pd.orc()
print(1000 * r + 4 * c + pd.d)