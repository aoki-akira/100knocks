N = 10

with open("chapter02/popular-names.txt", "r") as f:
    lines = f.readlines()

for line in lines[:N]:
    print(line, end="")