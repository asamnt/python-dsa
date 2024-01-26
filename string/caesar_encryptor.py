def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_map = {}
    new_array = []
    #make a map of char and its location in the alphabet sequence
    for i in range(len(alphabets)):
        alphabets_map[alphabets[i]] = i
    # loop through the string , get the index of the char, move the index by key
    # if the index is greater then 25, wrap around means modulo 26 , will give remainder which will be the new index from start
    for char in string:
        if char in alphabets_map:
            index = alphabets_map[char]

            new_index = index + key
            if new_index > 25:
                new_index = new_index % 26
            new_array.append(alphabets[new_index])
    return "".join(new_array)


print(caesarCipherEncryptor("abc", 4))
