
import random

def typoglycemia(text):
    words = text.split()
    result = []

    for word in words:
        if len(word) > 4:
            middle = list(word[1:-1])
            random.shuffle(middle)
            new_word = word[0] + "".join(middle) + word[-1]
            result.append(new_word)
        else:
            result.append(word)

    return " ".join(result)


sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(typoglycemia(sentence))
