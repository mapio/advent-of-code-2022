import fileinput

tot = 0

for line in fileinput.input():
  line = line.strip()
  r, s = set(line[:len(line)//2]), set(line[len(line)//2:])
  d = list(r & s)[0]
  r, s = ord(d) - ord('a'), ord(d) - ord('A')
  tot += r + 1 if r >= 0 else s + 27

print(tot)