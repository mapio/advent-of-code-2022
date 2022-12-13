import fileinput
from functools import cmp_to_key

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
pairs = [[[2]], [[6]]]
try:
  while True:
    l0 = next(it).strip()
    l1 = next(it).strip()
    pairs.extend([eval(l0), eval(l1)])
    next(it)
except StopIteration:
  pass

s = sorted(pairs, key = cmp_to_key(cmp))

print((1 + s.index([[2]])) * (1 + s.index([[6]])))