with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines[:10]:
    print(line.replace("\t", " "), end="")