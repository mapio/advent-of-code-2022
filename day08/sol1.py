import numpy as np
import fileinput

M = np.array([list(map(int, line.strip())) for line in fileinput.input()])

v = 0
for i in range(1, len(M) - 1):
  for j in range(1, len(M[0]) - 1):
    t = M[i, j]
    v += 1 * any([
      all(t >M[i,:j]), 
      all(t> M[i,1 + j:]),
      all(t > M[:i,j]),
      all(t > M[1 + i:,j])
    ])
    
print(v)
