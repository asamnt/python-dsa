def run_length_encoding(string):
    encodedStringChar = []
    currentRunLength = 1

    for i in range(1 , len(string)):
        currentChar = string[i]
        prevChar = string[i-1]

        if currentChar != prevChar or currentRunLength == 9:
            encodedStringChar.append(str(currentRunLength))
            encodedStringChar.append(prevChar)
            currentRunLength = 0
        currentRunLength += 1
    
    #after loop finishes the last char remains to be added
    encodedStringChar.append(str(currentRunLength))
    encodedStringChar.append(string[len(string)-1])

    return "".join(encodedStringChar)

print(run_length_encoding("AAAAAAABBBCCCFFFM"))


