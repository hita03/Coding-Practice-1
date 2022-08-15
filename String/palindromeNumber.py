# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.
 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    
    # def rev(self,n,li):
    #     rem=None
    #     while n!=0:
    #         rem = n%10
    #         n/=10
    #         li.append(rem)
    #     return li
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: 
            return False
        
        n=str(x)
        nrev=n[::-1]
        
        for i in range(len(n)):
            if n[i]!=nrev[i]:
                return False
        
        return True
            