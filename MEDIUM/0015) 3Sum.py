"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

def threeSum(nums):
    
    nums.sort()
    ans = []
    
    for i in range(len(nums)-2):
        if(nums[i] > 0):
            break
        
        if(nums[i] < -2*nums[-1]):
            continue
        
        if(i>0 and nums[i]==nums[i-1]):
            continue
        
        start, end = i+1, len(nums)-1
        while(start < end):
            sum = nums[i] + nums[start] + nums[end]
            if(sum < 0):
                start += 1
            elif(sum > 0):
                end -= 1
            else:
                ans.append([nums[i], nums[start], nums[end]])
                while(start < end and nums[start] == nums[start+1]):
                    start += 1
                while(start < end and nums[end] ==  nums[end-1]):
                    end -= 1
                start += 1
                end -= 1
        
    return ans


""" Second Method """

def threeSum(nums):
    if len(nums) < 3:
            return []
    nums.sort()
    res = []
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.append((v, -v-x, x))
    return res
