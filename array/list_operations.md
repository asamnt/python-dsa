List operations

l.append(30) - will append 30 to the end of the list l
l.insert(1, 15) - will insert 15 at index 1 in list l
print(15, l) - will print true if 15 present in list l
print(l.count(30)) - will count the number of times 30 present in list l

//use index function carefully as if item not present it will raise value error
print(l.index(30)) - will give index of first occurence
print(l.index(30, 4, 7)) - search between indices 4 and 6

//use remove function carefully as if item not present it will raise value error
l.remove(20)

l.pop() - removes the last item from the list and returns it
l.pop(2) - remove the item at given index and returns the item

del l[1] - remove the item at index 1

del[0:2] - remove the items from index 0 to 1

max(l) - max item in list
min(l) - min item in the list
sum(l) - sum of items in list
l.reverse()
l.sort()
