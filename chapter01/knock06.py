def ngram(sequence, n):
    result = []

    for i in range(len(sequence) - n + 1):
        result.append(sequence[i:i+n])

    return result

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)