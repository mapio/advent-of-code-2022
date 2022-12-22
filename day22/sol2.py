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
N = len(M) // 3

MP = [(row + [' '] * C)[:C] for row in M]
M = MP
MD = [row[:] for row in M]

#MOVES = next(it).strip()

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

#     D
# A B C
#     E F

def step(pd):
  r, c = pd.rc
  if pd.d in {0, 2}: # H
    if r < N: # D
      if c == 2 * N - 1 and pd.d == 2: # D -> B
        print('D->B')
        pd.rc = np.array([N, N + r])
        pd.d = 1
        return pd
      if c == 3 * N - 1 and pd.d == 0: # D -> F
        print('D->F')
        pd.rc = np.array([3 * N - 1 - r, 4 * N - 1])
        print(pd.rc)
        pd.d = 2
        return pd
    # elif r < 2 * N:
    # else:
  pd.rc = pd.rc + DIR[pd.d]
  return pd

pd = PD(np.array([1, 9]), 2)
for i in range(7):
  print(pd, M[pd.rc[0]][pd.rc[1]])
  pd = step(pd)
