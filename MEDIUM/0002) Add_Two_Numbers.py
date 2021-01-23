"""
    https://leetcode.com/problems/add-two-numbers/
    
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    ans = t = ListNode()
    carry = 0
    while(l1 and l2):
        s = l1.val + l2.val + carry     
        l1 = l1.next
        l2 = l2.next
        t.next = ListNode(s%10)
        carry = int(s/10)
        t = t.next
    
    l3 = l1 or l2
    while(l3):
        s = l3.val + carry
        l3 = l3.next
        t.next = ListNode(s%10)
        carry = s//10
        t = t.next
        if(not carry):
            t.next = l3
            return ans.next
        
    if(carry):
        t.next = ListNode(carry)
        
    return ans.next



"""  Another Solution """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    ans = t = ListNode()
    carry = 0
    while(l1 or l2):
        s = 0
        if(l1):
            s += l1.val
            l1 = l1.next
        if(l2):
            s += l2.val
            l2 = l2.next
        s += carry
        t.next = ListNode(s%10)
        t = t.next
        carry = s//10
        
    if(carry):
        t.next = ListNode(carry)
        
    return ans.next
