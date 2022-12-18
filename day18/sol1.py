import numpy as np
from collections import Counter

def n(x, y, z):
  return {
    (x - 1, y    , z    ),
    (x + 1, y    , z    ),
    (x    , y - 1, z    ),
    (x    , y + 1, z    ),
    (x    , y    , z - 1),
    (x    , y    , z + 1),
  }

P = np.loadtxt('input.txt', delimiter = ',').astype(int)
N = Counter()
for x, y, z in P: N.update(n(x, y, z))

for p in P: del N[tuple(p)]

print(N.total())