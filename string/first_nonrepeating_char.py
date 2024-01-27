def firstNonRepeatingCharacter(string):
    # Write your code here.
    charFreq = {}
    #loop through the string
    # put all the chars in a map and increase the count everytime you encounter the same char again
    for char in string:
        charFreq[char] = charFreq.get(char,0)+1 #if you dont get the char, default count to zero
    for idx in range(len(string)):#loop though the string again and check the char count in the map
        char = string[idx]
        if charFreq[char] == 1:#the first char you see has count > 1, you return it
            return idx
    return -1
