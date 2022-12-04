import fileinput

tot = 0

tot = 0

for line in fileinput.input():
  a, b = line.strip().split(',')
  al, ar = list(map(int, a.split('-')))
  bl, br = list(map(int, b.split('-')))
  l, r = set(range(al, ar + 1)), set(range(bl, br + 1))
  if l & r: tot +=1

print(tot)