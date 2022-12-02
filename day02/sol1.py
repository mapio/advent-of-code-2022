import fileinput

move2pts = {
  'A X': 4,
  'A Y': 8,
  'A Z': 3,
  'B X': 1,
  'B Y': 5,
  'B Z': 9,
  'C X': 7,
  'C Y': 2,
  'C Z': 6
}

tot = 0
for l in fileinput.input():
  tot += move2pts[l.strip()]

print(tot)