def reverseLinkedList(head):
    # assign p1 as null and p2 as the first node, fpr p3 we will assign in the while loop
    p1, p2 = None, head
    while p2 is not None:
        p3 = p2.next # first assign the next node to p3 - so we have all variables assigned
        p2.next = p1 # reverse the node p2 to point to prev node that is p1

        #shifting forward
        p1 = p2 #now we are shifting forward so p1 moves to p2
        p2 = p3 # we are shifting forward sp p2 moves to p3
    return p1