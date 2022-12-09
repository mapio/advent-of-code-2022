import fileinput

class T:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.pos = set()
  def chase(self, head):
    if self.x == head.x and self.y == head.y: return
    if self.x == head.x and abs(self.y - head.y) == 2:
      self.y -= (self.y - head.y) // 2
    elif self.y == head.y and abs(self.x - head.x) == 2:
      self.x -= (self.x - head.x) // 2
    else:
      dx = self.x - head.x
      dy = self.y - head.y
      if abs(dx) == 1 and abs(dy) == 2:
        self.x -= dx
        self.y -= dy // 2
      elif abs(dx) == 2 and abs(dy) == 1:
        self.x -= dx // 2
        self.y -= dy
    self.pos.add((self.x, self.y))
  def __repr__(self):
    return f'T({self.x}, {self.y})'

class H:
  def __init__(self, tail):
    self.x = 0
    self.y = 0
    self.tail = tail
  def move(self, dir):
    if dir == 'U':
      self.y +=1
    elif dir == 'D':
      self.y -=1
    elif dir == 'L':
      self.x -= 1
    elif dir == 'R':
      self.x += 1
    self.tail.chase(self)
  def moves(self, dir, steps):
      for _ in range(steps): self.move(dir)
  def __repr__(self):
    return f'H({self.x}, {self.y})'

t = T()
h = H(t)

def _print(h, t, n):
  for y in range(n, -1, -1):
    for x in range(n):
      if h.x == x and h.y == y: print('H', end = '')
      elif t.x == x and t.y == y: print('T', end = '')
      else: print('.', end = '')
    print()
  print('=' * n)

for line in fileinput.input():
  d, n = line.strip().split()
  h.moves(d, int(n))

print(len(t.pos))
