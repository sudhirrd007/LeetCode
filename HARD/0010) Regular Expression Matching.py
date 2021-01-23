"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false
"""

def isMatch(self, s: str, p: str) -> bool:
    
    temp = ""
    for i in p:
        if(i == "*"):
            temp = temp[:-1]
            break
        temp += i
    if(temp == s[:len(temp)]):
        p = p[len(temp):]
        s = s[len(temp):]
    
    cmp = [[True if i==0 and j==0 else False for j in range(len(p)+1)] for i in range(len(s)+1)]

    for l in range(1,len(p)+1):
        if(p[l-1] == "*"):
            cmp[0][l] = cmp[0][l-2]
        
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if(s[i-1] == p[j-1] or p[j-1] == "."):
                cmp[i][j] = cmp[i-1][j-1]
            elif(p[j-1] == "*"):
                cmp[i][j] = cmp[i][j-2]
                if(s[i-1] == p[j-1-1] or p[j-1-1] == "."):
                    cmp[i][j] = cmp[i][j] or cmp[i-1][j]
            else:
                cmp[i][j] = False

    return cmp[len(s)][len(p)]