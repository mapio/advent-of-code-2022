import fileinput

li = iter(fileinput.input())

status = []
for line in li:
  if '[' not in line: break
  status.append(line.rstrip())

num = int(line.strip().split()[-1])

stack = [[] for _ in range(num)]
for s in status:
  s += '   ' * num
  for i in range(num):
    l = s[1 + i * 4]
    if l != ' ': stack[i].append(l)

next(li)
for m in li:
  n, f, t = list(map(int, m.strip().split()[1::2]))
  take, stack[f - 1] = stack[f - 1][:n], stack[f - 1][n:]
  stack[t - 1] = take[::-1] + stack[t - 1]

print(''.join(s[0] for s in stack))