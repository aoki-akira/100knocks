sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split()

result = []

for word in words:
    result.append(len(word))

print(result)