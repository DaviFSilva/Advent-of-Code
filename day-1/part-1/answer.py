input = open("input.txt")
numbers = ["0","1","2","3","4","5","6","7","8","9"]
line_value = []
result = 0

for line in input.readlines():
  line_value = []
  for c in line:
    if c in numbers:
      line_value.append(int(c))
  result += line_value[0]*10
  result += line_value[-1]

print(result)