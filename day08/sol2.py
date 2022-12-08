import numpy as np
import fileinput

M = np.array([list(map(int, line.strip())) for line in fileinput.input()])

def tlen(v, t):
  r = 0
  for x in v:
    r += 1
    if x >= t: break
  return r

max = 0
for i in range(1, len(M) - 1):
  for j in range(1, len(M[0]) - 1):
    t = M[i, j]
    v = tlen(M[i,:j][::-1], t) * tlen(M[i,1 + j:], t) * tlen(M[:i,j][::-1], t) * tlen(M[1 + i:,j], t)
    if v > max: max = v

print(max)