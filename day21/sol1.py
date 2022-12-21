import fileinput
import networkx as nx
from operator import add, mul, floordiv, sub

G = nx.DiGraph()

node2val = dict()
node2op = dict()

op2f = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': floordiv
}

for line in fileinput.input():
  monkey, job = line.strip().split(':')
  js = job.strip().split(' ')
  if len(js) == 1:
    node2val[monkey] = int(job)
  else:
    left, op, right = js
    node2op[monkey] = op
    G.add_edge(left, monkey)
    G.add_edge(right, monkey)

for node in list(nx.topological_sort(G)):
  if node in node2op:
    left, right = G.in_edges(node)
    node2val[node] = op2f[node2op[node]](node2val[left[0]], node2val[right[0]])

print(node2val['root'])