def longestSubstringWithoutDuplication(string):
    # Write your code here.
    # maintain a hashmap of char and its last seen position
    # this will help us to know if the char was present in the string earlier and what was its index
    # then we can compare if its index is falling within the current substring
    lastSeen = {}
    #starting substring is first char
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            #if we see a char in the map, then we check if the starting index of the current substring is greater than the last seen index of the char, whichever is the greater index we keep as the startidx
            # if the current start index is greater it means the char is not repeating in the current substring, hence we dont worry
            # if the current start index is lesser than the last seen index of the char, it means we have two instances of the char - one at last seen index and one current char
            #so we then shift the starting index to the index one after the last seen index of current char
            startIdx = max(startIdx , lastSeen[char]+1)
        
        # after every char, we check if the current substring is greater than existing substring
            # current substring = (current index i + 1) minus startidx
            # existing longest substring in the longest array
        if longest[1] - longest[0] < (i + 1) - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i#update the last seen index of char
    return string[longest[0]:longest[1]]