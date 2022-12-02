import fileinput
import heapq

best_three = []
tot = 0
for l in fileinput.input():
  if not l.strip():
    print(tot)
    if len(best_three) < 3:
      heapq.heappush(best_three, tot)
    else:
      heapq.heappushpop(best_three, tot)
    tot = 0
  else:
    tot += int(l.strip())
if len(best_three) < 3:
  heapq.heappush(best_three, tot)
else:
  heapq.heappushpop(best_three, tot)

print(sum(best_three))