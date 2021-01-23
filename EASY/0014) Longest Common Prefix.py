"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()
        ans = strs[0]

        for i in strs:
            for j in range(len(ans)):
                if(ans[j] != i[j]):
                    ans = ans[:j]
                    break
        return ans

""" Another Faster method """

def longestCommonPrefix(self, strs: List[str]) -> str:
        
    if not strs:
        return ""
    
    s1 = min(strs)
    s2 = max(strs)

    for index, val in enumerate(s1):
        if(val != s2[index]):
            return s1[:index]
    
    return s1
