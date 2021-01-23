"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getDecimalValue(head):  # head : ListNode
    
    sum = []
    temp = head
    while(temp):
        sum.append(temp.val)
        temp = temp.next
    
    ans = 0
    for count,i in enumerate(sum[::-1]):
        ans += 2**count * i
    
    return ans


""" Fast Method """

def getDecimalValue(head):  # head : ListNode
    ans = 0
    while head:
        ans = (ans << 1) + head.val  # ans = (ans << 1) | head.val
        head = head.next
    return ans
