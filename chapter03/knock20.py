
import gzip
import json

with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:

    for line in f:

        data = json.loads(line)

        if data["title"] == "イギリス":

            print(data["text"])

            break
