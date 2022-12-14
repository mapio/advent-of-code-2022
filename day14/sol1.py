import fileinput

def xy(s):
  x, y = s.strip().split(',')
  return int(x), int(y)

def p():
  for y in range(0, maxy + 1):
    for x in range(minx - 1, maxx + 2):
      print('.' if (x,y) not in G else '#', end = '')
    print()

def sand():
  x, y = 500, 0
  while y < maxy:
    nx = x
    ny = y + 1
    if (nx, ny) in G:
      nx = x - 1
      if (nx, ny) in G:
        nx = x + 1
        if (nx, ny) in G:
          G.add((x, y))
          return True
    x, y = nx, ny
  return False

G = set()
maxy = 0
minx = 1000
maxx = 0
for line in fileinput.input():
  prev, *rest = line.strip().split('->')
  px, py = xy(prev)
  if py > maxy: maxy = py
  if px < minx: minx = px
  if px > maxx: maxx = px
  for nxt in rest:
    nx, ny = xy(nxt)
    if ny > maxy: maxy = ny
    if nx < minx: minx = nx
    if nx > maxx: maxx = nx
    if px == nx:
      a, b = min(py, ny), max(py, ny)
      for y in range(a, b + 1): G.add((px, y))
    else:
      a, b = min(px, nx), max(px, nx)
      for x in range(a, b + 1): G.add((x, py))
    px, py = nx, ny

n = 0

while sand(): n += 1

print(n)