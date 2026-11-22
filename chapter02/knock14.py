with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines[:10]:
    name = line.split("\t")[0]
    print(name)