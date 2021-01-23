"""
 https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
 
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        sum = 0

        for i in str(n):
            sum += int(i)
            product *= int(i)

        return product - sum


# Other Solution

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum, prod = 0, 1
        while n:
            n, digit = divmod(n, 10)
            sum += digit
            prod *= digit
        return prod - sum        
