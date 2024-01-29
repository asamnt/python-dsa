# O(n) Time
def isPalindrome(string):
    # Write your code here.
    n = len(string)
    mid = len(string)//2
    for i in range(mid):
        if string[i]!=string[n-1-i]:
            return False
    return True

print(isPalindrome("aaabaaaa"))