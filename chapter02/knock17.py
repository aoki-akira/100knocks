with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

names = []

for line in lines:
    name = line.split("\t")[0]
    names.append(name)

unique_names = set(names)

for name in unique_names:
    print(name)