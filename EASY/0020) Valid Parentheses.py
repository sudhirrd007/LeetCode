"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

def isValid(self, s: str) -> bool:
    print(s)
    if(len(s) % 2 != 0):
        return False
    
    if(s.count("(") != s.count(")") or 
       s.count("]") != s.count("]") or 
       s.count("{") != s.count("}")):
        return False
    
    
    stack_data = []
    
    round_b = ["(", ")"]
    square_b = ["[", "]"]
    curly_b = ["{", "}"]
    
    open_b = ["(", "[", "{"]
    close_b = [")", "]", "}"]
        
    for curr in range(len(s)):
        if(curr > 0):
            if(s[curr] in close_b and s[curr-1] in open_b): 
                if(open_b.index(s[curr-1]) != close_b.index(s[curr])):
                    return False
                else:
                    stack_data.pop()
                    continue
            
        if(s[curr] == round_b[0]):
            stack_data.append(round_b[1])
        elif(s[curr] == square_b[0]):
            stack_data.append(square_b[1])
        elif(s[curr] == curly_b[0]):
            stack_data.append(curly_b[1])
        elif(s[curr] in close_b and len(stack_data) > 0):
            if(s[curr] != stack_data[-1]):
                return False
            else:
                stack_data.pop()
    return True


""" Other Method """
def isValid(self, s: str) -> bool:
    bracket_map = {"}":"{", ")":"(", "]":"["}
    open_b = ["{", "(", "["]
    open_stack = [False]
    open_count = 0

    for b in s:
        if b not in ["{", "}", "(", ")", "[", "]"]:
            return False
        elif b in open_b:
            open_stack.append(b)
            open_count += 1
        elif bracket_map[b] == open_stack[open_count]:
            open_stack.pop()
            open_count -= 1
        else:
            return False
        
    return open_count == 0


""" Fast Method(Same like above one) """
def isValid(self, s: str) -> bool:
    st, pair = [], {")": "(", "}": "{", "]": "["}
    for c in s:
        if st and c in pair and pair[c] == st[-1]: st.pop()
        else: st.append(c)
    return not st


""" Very Fast Solution """
def isValid(self, s):
    stack = ['#']
    for c in s:
        if c == '(': stack.append(')')
        elif c == '{': stack.append('}')
        elif c == '[': stack.append(']')
        elif c != stack.pop(): return False
    return stack == ['#']