import re

input = open("input.txt")

numbers = ["1","2","3","4","5","6","7","8","9"]
spelled_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

line_value = []
result = 0

for line in input.readlines():
  line_value.clear()

  for character in range(len(line)):
    if line[character] in numbers:
      line_value.append({"index": character, "value": int(line[character])})

  for number in spelled_numbers:
    if number in line:
      ocurrences_indices = [i.start() for i in re.finditer(number, line)]
      for index in ocurrences_indices:
        line_value.append({"index": index, "value": numbers[spelled_numbers.index(number)]})

  line_value.sort(key=lambda x: x["index"])

  result += int(line_value[0]["value"])*10
  result += int(line_value[-1]["value"])

print(result)