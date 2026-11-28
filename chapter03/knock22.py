import gzip
import json
import re

with gzip.open("chapter03/jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    articles = [json.loads(line) for line in f]

for article in articles:
    if article["title"] == "イギリス":
        text = article["text"]
        break

categories = re.findall(r"\[\[Category:([^|\]]+)", text)

with open("chapter03/out/knock22.txt", "w", encoding="utf-8") as f:
    for category in categories:
        print(category, file=f)