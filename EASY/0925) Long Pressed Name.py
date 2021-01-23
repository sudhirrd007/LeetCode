"""
Your friend is typing his name into a keyboard.  
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""

def isLongPressedName(self, name: str, typed: str) -> bool:
    if(name[0] != typed[0] or name[-1] != typed[-1]):
        return False        

    i = 0
    L = len(name) 
    for j in typed:
        if(i < L and name[i] == j):
            i += 1
        elif(not name[i-1] == j):
            return False
    return True


###### Another
def isLongPressedName(self, name: str, typed: str) -> bool:
    if(name[0] != typed[0] or name[-1] != typed[-1]):
        return False        

    name = [(k, len(list(grp))) for k,grp in itertools.groupby(name)]
    typed = [(k, len(list(grp))) for k,grp in itertools.groupby(typed)]
    
    if(len(name) != len(typed)): # because both are list of tuples of characters
        return False
    
    return all(k1==k2 and v1<=v2 for (k1,v1),(k2,v2) in zip (name,typed))
