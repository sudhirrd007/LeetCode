"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""

def lengthOfLongestSubstring(self, s):
    ans = dict()
    for n in range(s.__len__()):
        temp = ""
        temp_dict = []
        for val in range(n, s.__len__()):
            if(s[val] in temp_dict):
                ans[temp] = temp.__len__()
                break
            temp += s[val]
            temp_dict.append(s[val])
        else:
            ans[temp] = temp.__len__()

    ans = sorted(ans.items(), key=lambda num:num[1], reverse=True)
    
    if(bool(ans)):
        return ans[0][1]
    elif(s.__len__() > 0):
        return 1
    else:
        return 0