import gzip
import json

with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:

    for line in f:
        data = json.loads(line)

        if data["title"] == "イギリス":

            for text_line in data["text"].splitlines():

                if "Category:" in text_line:
                    print(text_line)

            break
