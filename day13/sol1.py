import fileinput

def cmp(a, b):
  while a and b:
    fa, *a = a
    fb, *b = b
    if isinstance(fa, int) and isinstance(fb, int):
      if fa < fb: return -1
      elif fa > fb: return 1
      else: continue
    c = 0
    if isinstance(fa, int) and isinstance(fb, list): 
      c = cmp([fa], fb)
    elif isinstance(fa, list) and isinstance(fb, int):
      c = cmp(fa, [fb])
    else:
      c = cmp(fa, fb)
    if c: return c
  if not a and not b: return 0
  if not a: return -1
  elif not b: return 1
  else: raise RuntimeError('Something went wrong')

it = iter(fileinput.input())
idx = 1
sum = 0
try:
  while True:
    l0 = next(it).strip()
    l1 = next(it).strip()
    pair = eval(l0), eval(l1)
    next(it)
    if cmp(*pair) == -1: sum += idx
    idx += 1
except StopIteration:
  pass

print(sum)