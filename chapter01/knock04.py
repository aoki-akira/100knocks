sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sentence.split()

result = {}

for i, word in enumerate(words, start=1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        result[word[0]] = i
    else:
        result[word[:2]] = i

print(result)