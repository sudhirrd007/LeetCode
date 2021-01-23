"""
    https://leetcode.com/problems/container-with-most-water/
    
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height) -> int:
    i, j = 0, len(height)-1 
    ans = j*min(height[i], height[j])

    while(i<j):
        if(height[i] < height[j]):
            i += 1
        elif(height[i] > height[j]):
            j -= 1
        else:
            i += 1
            j -= 1
        ans = max(ans, (j-i)*min(height[i], height[j]))

    return ans

ans = maxArea([1,8,6,2,5,4,8,3,7])
