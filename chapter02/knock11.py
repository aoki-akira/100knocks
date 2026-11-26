N = 10

with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines[:N]:
    print(line, end="")