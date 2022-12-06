import fileinput

msg = next(fileinput.input()).strip()

for p in range(4, len(msg) - 3):
  som = msg[p - 4:p]
  if len(set(som)) == 4:
    print(p)
    break
