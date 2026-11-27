import random

with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

random.shuffle(lines)

for line in lines:
    print(line, end="")