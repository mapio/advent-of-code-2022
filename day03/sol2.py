import fileinput

tot = 0

li = iter(fileinput.input())
while True:
  try:
    l0, l1, l2 = next(li), next(li), next(li)
    r, s, t = set(l0.strip()), set(l1.strip()), set(l2.strip())
    d = list(r & s & t)[0]
    r, s = ord(d) - ord('a'), ord(d) - ord('A')
    tot += r + 1 if r >= 0 else s + 27
  except StopIteration:
    break

print(tot)