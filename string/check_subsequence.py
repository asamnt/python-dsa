def is_subsequence(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1 # increment the smaller string idx only if we find a match
        i += 1 # always increment the longer string idx
    
    if j == len(s2):
        return True
    else:
        return False
    
#overhead of recursive calls
def is_subsequence_recursive(s1, s2, m, n):
    # this means we have reached end of the sequence string and hence it is a valid subsequence
    if n == 0:
        return True
    # this means we have finished parsing the main string and have not found a subsequence
    if m == 0:
        return False
    
    if s1[m-1] == s2[n-1] :
        return is_subsequence_recursive(s1, s2, m-1, n-1)
    else:
        return is_subsequence_recursive(s1, s2, m-1, n)


print(is_subsequence("geeksforgeeks","fork"))
print(is_subsequence_recursive("geeksforgeeks","fork", len("geeksforgeeks"), len("fork")))
    