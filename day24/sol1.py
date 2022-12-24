from collections import defaultdict
import fileinput
import networkx as nx

DIR = {
  '>': ( 0,  1),
  'v': ( 1,  0),
  '<': ( 0, -1),
  '^': (-1,  0)
}

MDIR = frozenset(DIR.keys())

MAP = defaultdict(list)
lines = [line.strip()[1:-1] for line in fileinput.input()][1:-1]
print(lines)
for r, line in enumerate(lines):
  for c, v in enumerate(line):
    if not v in MDIR: continue
    MAP[(r,c)].append(v)

R, C = len(lines), len(lines[0])
MAP = dict(MAP)
COORDS = frozenset((r, c) for r in range(R) for c in range(C))

def pm(m):
  print('#' * (C + 2))
  for r in range(R):
    print('#', end = '')
    for c in range(C):
      if (r, c) in m: 
        mrc = m[(r, c)]
        print(mrc[0] if len(mrc) == 1 else len(mrc), end = '')
      else:
        print('.', end = '')
    print('#')
  print('#' * (C + 2))

def move(rc, d):
  r, c = rc
  dr, dc = DIR[d]
  r = (r + dr) % R
  c = (c + dc) % C
  return (r, c)

def step(m):
  mp = defaultdict(list)
  for p, vs in m.items():
    for v in vs:
      mp[move(p, v)].append(v)
  return dict(mp)

G = nx.DiGraph()

mp = MAP
pm(mp)
n = 1
while True:
  print(n)
  G.add_node((-1, 0, n - 1))
  G.add_node((R, C - 1, n))
  coords = list((COORDS - set(mp.keys()))) + [(-1, 0)]
  mpp = step(mp)
  pcoords = list((COORDS - set(mpp.keys()))) + [(-1, 0), (R, C - 1)]
  for r, c in coords:
    for dr, dc in list(DIR.values()) + [(0, 0)]:
      rp, cp = r + dr, c + dc
      if (rp, cp) in pcoords:
        G.add_edge((r,c, n - 1), (rp, cp, n))

  if n % 100 == 0:
    maxr, maxc = -1, 0
    for t in nx.shortest_path(G, (-1, 0, 0)):
      maxr = max(maxr, t[0])
      maxc = max(maxc, t[1])
    print(n, (maxr, maxc))
    if (maxr, maxc) == (R, C - 1): break
  else:
    try:
      path = nx.shortest_path(G, (-1, 0, 0), (R, C - 1, n))
      print(len(path), path)
    except nx.exception.NetworkXNoPath:
      pass
    else:
      break
  
  mp = mpp
  n += 1