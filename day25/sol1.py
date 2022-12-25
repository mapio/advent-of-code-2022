import fileinput

d2v = {
  '2': 2,
  '1': 1,
  '0': 0,
  '-': -1,
  '=': -2
}

v2d = {
  -2: '=',
  -1: '-',
   0: '0',
   1: '1',
   2: '2'
}

powers = []
p = 1
for _ in range(50):
  powers.append(p)
  p *= 5


def snafu2val(snafu):
  num = 0
  for d, p in zip(reversed(snafu), powers):
    num += d2v[d] * p
  return num

def val2snafu(n, k):
  d = []
  n5 = n + 2 * sum(powers[:k])
  while n5 > 0:
    d.append(v2d[n5 % 5 - 2])
    n5 //= 5
  return ''.join(reversed(d))

tot = 0
for line in fileinput.input():
  tot += snafu2val(line.strip())

for k in range(50):
  res = val2snafu(tot, k)
  if tot == snafu2val(res):
    print(res)
    break