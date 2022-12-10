import fileinput

vals = []
x = 1
for line in fileinput.input():
  if line.startswith('noop'):
    vals.append(x)
  else:
    d = int(line.split()[1])
    vals.extend([x, x])
    x += d
vals.append(x)

print(sum((i * vals[i - 1]) for i in range(20, 240, 40)))
