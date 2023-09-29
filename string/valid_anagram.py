from types import List
class Solution:
    def is_anagram(self, s: str, t:str) -> bool:
        return sorted(s) == sorted(t)
        
        return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            # building the hashmaps
            countS[s[i]] = 1 + countS.get(s[i],0) #we use get so that if the char does not exist, we can use default
            countS[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
    # we can sort the two strings and compare them, if they are the same then it is anagram, but time complexity could be n2