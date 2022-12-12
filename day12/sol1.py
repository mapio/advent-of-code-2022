import fileinput

M = [list(line.strip()) for line in fileinput.input()]

def h(c):
  if c == 'S': c = 'a'
  elif c == 'E': c = 'z'
  return ord(c) - ord('a')

def m(p):
  return M[p[0]][p[1]]

def b(p):
  r, c = p
  if r < 0 or r >= len(M): return False
  if c < 0 or c >= len(M[0]): return False
  return True

def n(p, q):
  if not (b(p) and b(q)): return False
  return h(m(q)) - h(m(p)) <= 1

import networkx as nx

G = nx.DiGraph()

S, E = None, None
for r in range(len(M)):
  for c in range(len(M[0])):
    p = (r, c)
    if m(p) == 'S': S = p
    if m(p) == 'E': E = p
    for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
      q = (r + dr, c + dc)
      if n(p, q): G.add_edge(p, q)

print(len(nx.shortest_path(G, S, E)) - 1)