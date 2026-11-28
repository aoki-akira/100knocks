import gzip
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

with gzip.open("chapter03/jawiki-country.json.gz", "rt", encoding="utf-8") as f:

    for line in f:

        data = json.loads(line)

        if data["title"] == "イギリス":

            print(data["text"])

            break