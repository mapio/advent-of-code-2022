import fileinput

maxsofar = 0
tot = 0
for l in fileinput.input():
  if not l.strip():
    if tot > maxsofar: maxsofar = tot
    tot = 0
  else:
    tot += int(l.strip())

print(maxsofar)