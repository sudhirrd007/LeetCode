"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    curr = head
    count = 1
    while(curr):
        curr = curr.next
        count += 1
    
    curr = head
    ans = t = ListNode()
    for v in range(count-n-1):
        t.next = ListNode(curr.val)
        t = t.next
        curr = curr.next

    t.next = curr.next

    return ans.next


""" Another Method """
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    fast=slow=head
    for i in range(n):
        fast=fast.next
    
    if not fast:
        return head.next
    
    while fast.next:
        fast=fast.next
        slow=slow.next
    slow.next=slow.next.next
    return head


""" Fast Method """
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    
    if head is None:
        return
    if head.next is None:
        return None
    
    records = []
    
    res = head
    
    while(head != None):
        records.append(head)
        head = head.next
        
    if len(records)  == n:
        res = res.next
    elif n == 1:
        records[len(records) - 2].next = None
    else:
        records[len(records) - n - 1].next = records[len(records) - n + 1]
    
    return res
