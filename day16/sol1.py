import fileinput
import re
import networkx as nx

P = re.compile(r'Valve (?P<frm>..) has flow rate=(?P<flow>\d+); tunnels? leads? to valves? (?P<dst>((..)(, )?)+)')

graph = nx.DiGraph()
flow = dict()
for line in fileinput.input():
  d = P.match(line).groupdict()
  for dst in d['dst'].split(', '): graph.add_edge(d['frm'], dst)
  f = int(d['flow'])
  if f > 0: flow[d['frm']] = f

shortest_paths = dict(nx.shortest_path_length(graph))

def solve(u, time, opened, value, solution):
  solution[opened] = max(solution.get(opened, 0), value)
  for v in set(flow.keys()) - set(opened):
    remaining_time = time - shortest_paths[u][v] - 1
    if remaining_time < 0: continue
    solve(v, remaining_time, frozenset(opened | {v}), value + remaining_time * flow[v], solution)
  return solution

print(max(solve('AA', 30, frozenset(), 0, dict()).values()))
