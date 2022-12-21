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

TS = [node for node in list(nx.topological_sort(G))[:-1] if node in node2op]

def comp(x):
  node2val['humn'] = x
  for node in TS:
    left, right = G.in_edges(node)
    node2val[node] = op2f[node2op[node]](node2val[left[0]], node2val[right[0]])
  left, right = G.in_edges('root')
  return node2val[left[0]], node2val[right[0]]

low = 0
high = 1
target = comp(0)[1]

while True:
  x, _ = comp(high)
  if x < target: break # invert for input0
  high *= 2

while low < high:
  x = (low + high) // 2
  a, b = comp(x)
  if a == b: break
  if a < target: # invert for input0
    high = x
  else: 
    low = x

sol = 0
for y in range(x, 0, -1):
  a, b = comp(y)
  if a != b: break
  sol = y

print(sol)