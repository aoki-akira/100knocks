sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split()

result = []

for word in words:
    word = word.strip(".,")
    result.append(len(word))

print(result)