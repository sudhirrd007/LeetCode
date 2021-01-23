"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

def letterCombinations(digits):
    
    d = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'],
     5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'],
     8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

    digits = list(map(int,digits))

    if(len(digits) == 0):
        return []
    if(len(digits) == 1):
        return d[digits[0]]

    ans = d[digits[0]]
    for i in range(1, len(digits)):
        temp = []
        for j in range(len(ans)):
            for k in d[digits[i]]:
                temp.append(ans[j]+k)
        ans = temp
        
    return ans


""" Second Method """

def letterCombinations(digits):
         
        d = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'],
         5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'],
         8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

        digits = list(map(int,digits))

        if(len(digits) == 0):
            return []
        if(len(digits) == 1):
            return d[digits[0]]

        ans = d[digits[0]] + []
        for i in range(1,len(digits)):
            L = len(ans)
            for j in range(L):
                for k in d[digits[i]]:
                    ans.append(ans[j]+k)
            ans = ans[L:]

        return ans
