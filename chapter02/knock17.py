with open("chapter02/popular-names.txt", "r", encoding="unf-8") as f:
    lines = f,readlines()

names = []

for line in lines:
    name = line.split("\t")[0]
    names.append(name)

unique_names = set(names)

print(len(unique_names))