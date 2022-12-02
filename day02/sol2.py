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

# X Y Z = l d w
result2move = {
  'A X': 'Z',
  'A Y': 'X',
  'A Z': 'Y',
  'B X': 'X',
  'B Y': 'Y',
  'B Z': 'Z',
  'C X': 'Y',
  'C Y': 'Z',
  'C Z': 'X'
}
tot = 0
for l in fileinput.input():
  l = l.strip()
  move = result2move[l]
  l = l[:2] + move
  tot += move2pts[l]

print(tot)