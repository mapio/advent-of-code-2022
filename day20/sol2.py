from dataclasses import dataclass
from itertools import starmap 
from pathlib import Path

@dataclass
class PosVal:
  pos: int
  val: int
  @classmethod
  def fromiterable(cls, it):
    return list(starmap(cls, enumerate(it)))

def find(pv, pos):
  for pv in pv: 
    if pv.pos == pos: return pv

def find0(pv):
  for ipv in PV:
    if ipv.val == 0: return ipv.pos

def move(pv, idx):
  lpv = pv[idx]
  pin = lpv.pos
  pfi = 1 + (pin + lpv.val - 1) % (len(pv) - 1)
  #print(lpv, pin, pfi)
  if pfi < pin:
    for ipv in pv:
      if pfi <= ipv.pos < pin: ipv.pos += 1
  elif pfi > pin:
    for ipv in pv:
      if pin < ipv.pos <= pfi: ipv.pos -= 1
  else:
    return
  lpv.pos = pfi
  return pv

OV = list(map(int, Path('input.txt').read_text().splitlines()))
DK = 811589153
V = [v * DK for v in OV]

PV = PosVal.fromiterable(V)
for r in range(10):
  for idx in range(len(PV)): move(PV, idx)

idx = find0(PV)
print(find(PV, (idx + 1000) % len(PV)).val + find(PV, (idx + 2000) % len(PV)).val + find(PV, (idx + 3000) % len(PV)).val)

