"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

==> Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.

==> Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
"""

def maximum69Number (self, num: int) -> int:
    num = str(num)
    for i in range(len(num)):
        if(num[i] == "6"):
            num = num[:i] + "9" + num[i+1:]
            break        
    return num


""" Other method without using of string """

def maximum69Number (self, num: int) -> int:
    ans = 0
    l = len(str(num)) - 1
    
    for i in range(l, -1, -1):
        temp = int(num / 10**i)
        if(temp == 6):
            temp = 9
            num = num % 10**i
            ans = ans*(10**(i+1)) + temp*(10**i) + num
            break
        num = num % 10**i
        ans = ans*10 + temp
    return ans
    