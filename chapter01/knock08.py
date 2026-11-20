def cipher(text):
    result = ""

    for char in text:
        if "a" <= char <= "z":
            result += chr(219 - ord(char))
        else:
            result += char

    return result

message = "I am student."
encrypted = cipher(message)

print(encrypted)
print(cipher(encrypted))