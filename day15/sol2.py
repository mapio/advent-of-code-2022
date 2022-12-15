import fileinput
import re
from tqdm import trange

import portion as I

P = re.compile(r'(-?\d+)')

def md(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

B, S, D = [], [], []
for line in fileinput.input():
  sx, sy, bx, by = list(map(int, P.findall(line)))
  S.append((sx, sy))
  B.append((bx, by))
  D.append(md((sx, sy), (bx, by)))

ub = 4_000_000
BOUND = I.closed(0, ub)

for y in trange(ub, 0 - 1, -1):
  i = None
  for (sx, sy), d in zip(S, D):
    d -= abs(y - sy)
    if d < 0: continue
    si = I.open(sx - d - 1, sx + d + 1)
    i = si if i is None else i | si
  res = BOUND - (i & BOUND)
  if not res.empty:
    l, u = res.lower, res.upper
    if l == u: print(l, y)
    else: print(f'TROUBLE at {y=}, {res=}')