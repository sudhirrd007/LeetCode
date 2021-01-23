"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    t = ListNode()
    ans = t
    if(not l1 or not l2):
        return l1 if l1 else l2
    
    while(l1 and l2):
        v1 = l1.val
        v2 = l2.val
        if(v1 < v2):
            ans.next = ListNode(v1)
            l1 = l1.next
        else:
            ans.next = ListNode(v2)
            l2 = l2.next
        ans = ans.next
        
    ans.next = l1 or l2
    # Same thing ------
    # if(l1):
    #     ans.next = l1
    # else:
    #     ans.next = l2
    #------------------
    
    return t.next


""" List Method """
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    l1_list = []
    if(l1):
        while(l1.next != None):
            l1_list.append(l1.val)
            l1 = l1.next
        l1_list.append(l1.val)
        
    l2_list = []
    if(l2):
        while(l2.next != None):
            l2_list.append(l2.val)
            l2 = l2.next
        l2_list.append(l2.val)

    l1_list.extend(l2_list)
    if(not l1_list):
        return l1
    l1_list.sort()
    
    
    node_lists = [ListNode(v) for v in l1_list]
    for index in range(len(node_lists)-1):
        node_lists[index].next = node_lists[index+1]
    
    return node_lists[0]


""" Fast Method """
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


""" Very Fast Method (Use Object Oriented Approach) """
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1 if l1 else l2
    elif l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1,l2.next)
        return l2