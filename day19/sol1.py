import fileinput 
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
import re

@dataclass(frozen = True, eq = True)
class ByKind:
  ore: int = 0 
  clay: int = 0 
  obsidian: int = 0 
  geode: int = 0
  def __add__(self, other):
    return ByKind(self.ore + other.ore, self.clay + other.clay, self.obsidian + other.obsidian, self.geode + other.geode)
  def __sub__(self, other):
    return ByKind(self.ore - other.ore, self.clay - other.clay, self.obsidian - other.obsidian, self.geode - other.geode)
  def __lt__(self, other):
    return all([self.ore < other.ore, self.clay < other.clay, self.obsidian < other.obsidian, self.geode < other.geode])
  def __le__(self, other):
    return all([self.ore <= other.ore, self.clay <= other.clay, self.obsidian <= other.obsidian, self.geode <= other.geode])

P = re.compile('(\d+)')
def parse(s):
  n = list(map(int, P.findall(s)))
  return n[0], {
    'ore': ByKind(ore = n[1]),
    'clay': ByKind(ore = n[2]),
    'obsidian': ByKind(ore = n[3], clay = n[4]),
    'geode': ByKind(ore = n[5], obsidian = n[6])
  }

def next_states(costs, r, o):
  if costs['geode'] <= o:
    yield r + ByKind(geode = 1), o - costs['geode'] + r
  if costs['obsidian'] <= o:
    yield r + ByKind(obsidian = 1), o - costs['obsidian'] + r
  if costs['clay'] <= o:
    yield r + ByKind(clay = 1), o - costs['clay'] + r
  if costs['ore'] <= o:
    yield r + ByKind(ore = 1), o - costs['ore'] + r
  yield r, o + r

MAX_T = 24

def visit(costs, r0, o0):

  maxval = 0
  highest = MAX_T

  SEEN = set()
  BEST_AT_D = {d: (ByKind(), ByKind()) for d in range(MAX_T + 1)}

  def _visit(r, o, d):
    nonlocal maxval, highest

    if (r, o, d) in SEEN: return
    SEEN.add((r, o, d))

    br, bo = BEST_AT_D[d]
    if r <= br and o <= bo: return
    if r > br and o > bo: BEST_AT_D[d] = r, o

    maxval = max(maxval, o.geode)
    if d >= MAX_T: return

    dt = MAX_T - d
    t2 = dt * (dt - 1) // 2
    maxr = 1 + min((o.ore + dt * r.ore + t2) // costs['geode'].ore, (o.obsidian + dt * r.obsidian + t2) // costs['geode'].obsidian)
    best = o.geode + dt * r.geode + (maxr * (maxr - 1) // 2)
    if best < maxval: return

    for rp, op in next_states(costs, r, o): _visit(rp, op, d + 1)

  _visit(r0, o0, 0)

  return maxval

with ProcessPoolExecutor() as executor:
    future_to_idx = dict() 
    for line in fileinput.input():
      idx, costs = parse(line)
      future_to_idx[executor.submit(visit, costs, ByKind(ore = 1), ByKind())] = idx
    sol = 0
    for future in as_completed(future_to_idx):
        idx = future_to_idx[future]
        try:
            val = future.result()
        except Exception as exc:
            print(f'blueprint {idx} generated an exception {exc}')
        else:
            print(f'blueprint {idx} value is {val}')
            sol += idx * val

print(f'Solution is: {sol}')

