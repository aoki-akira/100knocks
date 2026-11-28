import gzip
import json

with gzip.open("chapter03/jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)

        if data["title"] == "イギリス":

            with open("chapter03/out/knock21.txt", "w", encoding="utf-8") as out:
                for text_line in data["text"].splitlines():

                    if text_line.startswith("[[Category:"):
                        print(text_line, file=out)

            break