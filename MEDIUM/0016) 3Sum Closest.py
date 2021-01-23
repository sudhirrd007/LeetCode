"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def threeSumClosest(nums, target):
    
    nums.sort()
    ans = []
    L = len(nums)
    
    for index,i in enumerate(nums[:-2]):
        start, end = index+1, L-1
        
        if(i + nums[start] + nums[start+1] > target):
            ans.append(i + nums[start] + nums[start+1])
            
        elif(i + nums[end-1] + nums[end] < target):
            ans.append(i + nums[end-1] + nums[end])
        
        else:
            while(start < end):
                temp = i + nums[start] + nums[end]
                ans.append(temp)
                if(i + nums[start] + nums[end] < target):
                    start += 1
                elif(i + nums[start] + nums[end] > target):
                    end -= 1
                else:
                    return target

    ans.sort(key=lambda x:abs(x-target))
    return ans[0]
