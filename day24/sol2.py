from collections import defaultdict
import fileinput
import networkx as nx

from tqdm import tqdm 

DIR = {
  '>': ( 0,  1),
  'v': ( 1,  0),
  '<': ( 0, -1),
  '^': (-1,  0)
}

MDIR = frozenset(DIR.keys())

MAP = defaultdict(list)
lines = [line.strip()[1:-1] for line in fileinput.input()][1:-1]
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

def shortest(mp, src, dst):
  G = nx.DiGraph()
  n = 1
  while True:
    T.update()
    G.add_node((-1, 0, n - 1))
    G.add_node((R, C - 1, n))
    coords = list((COORDS - set(mp.keys()))) + [(-1, 0), (R, C - 1)]
    mpp = step(mp)
    pcoords = list((COORDS - set(mpp.keys()))) + [(-1, 0), (R, C - 1)]
    for r, c in coords:
      for dr, dc in list(DIR.values()) + [(0, 0)]:
        rp, cp = r + dr, c + dc
        if (rp, cp) in pcoords:
          G.add_edge((r,c, n - 1), (rp, cp, n))
    try:
      path = nx.shortest_path(G, (src[0], src[1], 0), (dst[0], dst[1], n))
    except nx.exception.NetworkXNoPath:
      pass
    else:
      return len(path) - 1, mpp    
    mp = mpp
    n += 1

T = tqdm()

a, mp = shortest(MAP, (-1, 0), (R, C - 1))
print(a)
b, mp = shortest(mp, (R, C - 1), (-1, 0))
print(b)
c, mp = shortest(mp, (-1, 0), (R, C - 1))

print(f'{a} + {b} + {c} = {a + b +c}')