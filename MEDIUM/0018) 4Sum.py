"""
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[ [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2] ]
"""

def fourSum(nums, target):

    nums.sort()
    L = len(nums)
    ans = []

    for i in range(L-3):
        if(i>0 and nums[i]==nums[i-1]):
            continue

        temp_target = -nums[i]+target

        for j in range(i+1, L-2):
            if(j>i+1 and nums[j] == nums[j-1]):
                continue
            start, end = j+1, L-1

            while(start < end):
                temp = nums[j] + nums[start] + nums[end]
                if(temp < temp_target):
                    start += 1
                elif(temp > temp_target):
                    end -= 1
                else:
                    temp = [nums[i], nums[j], nums[start], nums[end]]
                    if(temp not in ans):
                        ans.append(temp)
                    while(start < end and nums[start] == nums[start+1]):
                        start += 1
                    while(start < end and nums[end] == nums[end-1]):
                        end -= 1
                    start += 1
                    end -= 1        
    return ans



""" Speedy Method """

def fourSum(nums, target):

        nums.sort()
        L = len(nums)
        ans = []
        if(L > 2):
            last = nums[-1]
        else:
            return []

        for i in range(L-3):
            if(i>0 and nums[i]==nums[i-1] or nums[i] + 3*last < target):
                continue
            if(4*nums[i] > target):
                break

            for j in range(i+1, L-2):
                if(j>i+1 and nums[j] == nums[j-1] or nums[i]+nums[j]+2*last < target):
                    continue
                if(nums[i]+3*nums[j] > target):
                    break
                temp = nums[i] + nums[j]
                start,end = j+1, L-1
                
                while(start < end):
                    t = temp + nums[start] + nums[end]
                    if(t < target):
                        start += 1
                    elif(t > target):
                        end -= 1
                    else:
                        if([nums[i], nums[j], nums[end], t] not in ans):
                            ans.append([nums[i], nums[j], nums[start], nums[end]])
                        while(start < end and nums[start]==nums[start+1]):
                            start += 1
                        while(start < end and nums[end] == nums[end-1]):
                            end -= 1
                        start += 1
                        end -= 1
        return ans
