def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
    # maintain the map of sortedWord => list of actualWords
    for word in words:
        #sorted the chars in the word
        #so for example 'tac' becomes 'act'
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            #check if 'act' is already present in the map, if yes, add to the list pointed by 'act', the word 'tac'
            anagrams[sortedWord].append(word)
        else:#if 'act' is not present in the map, create a new key, value with key as 'act' and value as the word 'tac'
            anagrams[sortedWord] = [word]
    #return a list of the values from the maps
    return list(anagrams.values())

print(groupAnagrams(["oyo","yoo","gg"]))    