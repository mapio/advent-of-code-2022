from collections import Counter
import networkx as nx
import numpy as np

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

F = np.array(list(N.keys()))

def ext(p):
  def _ext(d):
    s = sorted({0, 1, 2} - {d})
    ff = P[(P[:,(s)] == p[s]).all(axis = 1)][:,d]
    if len(ff) == 0: return True
    return p[d] <= min(ff) or p[d] >= max(ff)
  p = np.array(p)
  return any((_ext(0), _ext(1), _ext(2)))

ARCS = set()
FS = set(map(tuple, F))
for u in FS:
  if ext(u): ARCS.add((u, 'OUT'))
  for v in n(*u) & FS:
    ARCS.add((u, v) if u < v else (v, u))

G = nx.Graph()
G.add_edges_from(ARCS)

sp = dict(nx.shortest_path_length(G))

tot = 0
for f in FS:
  if ext(f) or (f in sp and 'OUT' in sp[f]):
    tot += N[f]
print(tot)