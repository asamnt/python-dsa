def reverse_string(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        char = string[idx]

        #we get space char
        if char == " ":#if we get white space, we have a word which is from startOfWord to idx -1
            words.append(string[startOfWord:idx])
             # reset start of word to space
            startOfWord = idx
        #we get non space char
        elif string[startOfWord]==" ":# if the startofword is a space and we encounter a non sopace char in the iteration, we need to store the space in the list
            words.append(" ")
            startOfWord = idx
        
    words.append(string[startOfWord:])# add the last word
    print(words)
    reverseList(words)
    # print(words)
    return "".join(words)


def reverseList(list):
    start, end = 0, len(list)-1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1

print(reverse_string("India is the best"))



