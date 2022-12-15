import fileinput
import re
from operator import itemgetter
from tqdm import trange

P = re.compile(r'(-?\d+)')

def md(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

B, S, D = [], [], []
for line in fileinput.input():
  sx, sy, bx, by = list(map(int, P.findall(line)))
  S.append((sx, sy))
  B.append((bx, by))
  D.append(md((sx, sy), (bx, by)))

minx = min(s[0] - d for s, d in zip(S, D))
maxx = max(s[0] + d for s, d in zip(S, D))

y = 2_000_000
n = 0
print(maxx - minx)
for x in trange(minx - 1, maxx + 2):
  if any(md((x, y), s) <= d for s, d in zip(S, D)): n+= 1
  if (x, y) in B: n -= 1

print(n)
