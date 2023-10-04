def mergeList(a, b):
    result = []
    m, n = len(a), len(b)
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < m:
        result.append(a[i])
        i += 1
    while j < n:
        result.append(b[j])
        j += 1

    return result

a = [10, 15]
b = [5,6,7,40]
print(mergeList(a,b))

