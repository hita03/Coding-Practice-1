# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)-1
        i=0
        j=len(nums)-1
        res=[]
        while(i<=j and n>=0):
            if abs(nums[i]) > abs(nums[j]):
                res.append(nums[i]**2)
                i+=1

            else:
                res.append(nums[j]**2)
                j-=1
            # print(res," n=",n," i=",i," j= ",j)    
            n-=1 
        res.reverse()    
        return res        

            
        