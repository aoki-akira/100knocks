with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

names = []

for line in lines:
    name = line.split("\t")[0]
    names.append(name)

counts = {}

for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for name, count in sorted_counts:
    print(count, name)