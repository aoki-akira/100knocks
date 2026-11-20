def ngram(sequence, n):
    result = []

    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])
        
    return result

sentence = "I am an NLPer"

char_result = ngram(sentence, 3)

words = sentence.split()

word_result = ngram(words, 2)

print(char_result)
print(word_result)