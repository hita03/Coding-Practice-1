# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # li=[]
        # l=len(nums)
        # for i in range(l):
        #     li.append(nums[0:i] + nums[i+1:l])     
        # ans=[math.prod(ele)for ele in li]
        # return ans
        li=[]
        l=len(nums)
        if 0 not in nums:
            mul=math.prod(nums)
            return [int(mul/x) for x in nums]
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    li.append(math.prod(nums[0:i]+nums[i+1:l]))  
                   
                else:
                    li.append(0)
            return li
                    
                    
   
            