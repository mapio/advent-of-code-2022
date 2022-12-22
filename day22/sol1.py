from dataclasses import dataclass
import fileinput
import numpy as np
import re

it = iter(fileinput.input())

M = []
C = 0
for line in it:
  if not line.strip(): break
  C = max(C, len(line) - 1)
  M.append(list(line)[:-1])
R = len(M)

MP = [(row + [' '] * C)[:C] for row in M]
M = MP
MD = [row[:] for row in M]

MOVES = next(it).strip()

DIR = [
  np.array([ 0,  1]),
  np.array([ 1,  0]),
  np.array([ 0, -1]),
  np.array([-1,  0])
]

MDIR = ['>', 'v', '<', '^']

@dataclass
class PD:
  rc: np.array = np.array([0, 0])
  d: int = 0

def step(rc, d):
  while True:
    rc = rc + DIR[d]
    rc = np.array([rc[0] % R, rc[1] % C])
    m = M[rc[0]][rc[1]]
    if m != ' ': break
  return rc, m

def move(pd, dist):
  while dist > 0:
    orc = pd.rc
    pd.rc, m = step(pd.rc, pd.d)
    if m == '.': 
      MD[pd.rc[0]][pd.rc[1]] = MDIR[pd.d]
      dist -= 1
    elif m == '#': 
      pd.rc = orc
      break
    else:
      MD[pd.rc[0]][pd.rc[1]] = MDIR[pd.d]

pd = PD()
while M[0][pd.rc[1]] == ' ': pd.rc += DIR[pd.d]

for m in re.findall(r'\d+|R|L', MOVES):
  if m == 'R':
    pd.d = (pd.d + 1) % 4
  elif m == 'L':
    pd.d = (pd.d - 1) % 4
  else:
    move(pd, int(m))

r = 1 + (pd.rc[0] % R)
c = 1 + (pd.rc[1] % C)

print(1000 * r + 4 * c + pd.d)