with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=lambda line: int(line.split("\t")[2]), reverse=True)

for line in sorted_lines:
    print(line, end="")