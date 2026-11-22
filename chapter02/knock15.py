N = 10

with open("chapter02/popular-names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

total = len(lines)

for i in range(N):
    start = i * total // N
    end = (i + 1) * total // N

    with open(f"out/15_{i:02}.txt", "w", encoding="utf-8") as f:
        f.writelines(lines[start:end])