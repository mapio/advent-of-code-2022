import fileinput

msg = next(fileinput.input()).strip()

for p in range(14, len(msg)):
  som = msg[p - 14:p]
  if len(set(som)) == 14:
    print(p)
    break
