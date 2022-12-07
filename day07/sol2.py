import fileinput

class Dir:
  def __init__(self, name, parent = None):
    self.name = name 
    self.subdirs = dict()
    self.parent = parent
    self.files = dict()
    self.localsize = 0
  def addFile(self, name, size):
    self.files[name] = size
    self.localsize += size
  def addDir(self, name):
    d = Dir(name, self)
    self.subdirs[name] = d
    return d
  def getDir(self, name):
    if name == '..': return self.parent
    return self.subdirs[name]
  def size(self):
    return self.localsize + sum(s.size() for s in self.subdirs.values())
  def __str__(self):
    def _s(d, t = 0):
      res = [('  ' * t) + f'- {d.name} (dir)']
      res.extend(_s(sd,t + 1) for sd in d.subdirs.values())
      res.extend((('  ' * (t + 1)) + f'- {name} (file, {size=})' for name, size in d.files.items()))
      return '\n'.join(res)
    return _s(self)

root = Dir('/')
for line in fileinput.input():
  line = line.strip()
  if line == '$ cd /':
    curdir = root
  elif line.startswith('$ cd'):
    curdir = curdir.getDir(line[5:])
  elif line == '$ ls':
    pass
  elif line.startswith('dir '):
    curdir.addDir(line[4:])
  else:
    size, name = line.split()
    size = int(size)
    curdir.addFile(name, size)

TOTAL_SIZE = 70_000_000
REQUIRED = 30_000_000

SIZES = dict()
def sizes(d):
  SIZES[d.name] = d.size()
  for sd in d.subdirs.values(): sizes(sd)
sizes(root)

UNUSED = TOTAL_SIZE - root.size()
to_find = REQUIRED - UNUSED

candidates = [s for s in SIZES.values() if s >= to_find]

print(min(candidates))