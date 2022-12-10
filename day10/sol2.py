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

for r in range(6):
  for c in range(40):
    pos = r * 40 + c
    print('#' if (vals[pos] - 1 <= c <= vals[pos] + 1) else '.', end = '')
  print()