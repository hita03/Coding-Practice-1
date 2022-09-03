# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this section adds the frequency of characters in s to a dictionary
        d={}
        for char in s:
            if char not in d:
                d[char] = 1
            elif char in d:
                d[char]+=1
        
        # count_even holds those characters that have even frequency
        # count_odd holds those characters that have odd frequency
        # following section appends even/odd frequency chars to their respective lists.
        count_even = []
        count_odd = []
        
        for char in d:
            if d[char] %2 == 0:
                count_even.append(d[char])
            
            else:
                count_odd.append(d[char])
        
        
        # greedy approach follows the longest palindrome as -  all the even occurences + largest odd centre point + largest even number of odd frequency chars
        # largest even number of odd frequency chars -- 
        # suppose count_odd = [23,17,89,91]
        # max(count_odd) = 91 = center point
        # but we can also include 88 chars, 16, and 22 on either side of the centre point and increase lt. of palindrome
        # sum(odd_count_subset) - len(odd_count_subset) takes care of this
        if len(count_odd) !=0:
            odd_count_subset =[]
            for x in count_odd:
                
                if(x != max(count_odd) and x>1):
                    print(x)
                    odd_count_subset.append(x)
                    
            max_count = count_odd.count(max(count_odd)) 
            
            # this if construct takes care of multiplte max occurences of characters, e.g = [15,67,87,91,91]
            # one of the max values will be the center point;  the rest will be added to odd_count_subset
            if max_count !=1:
                for x in range(max_count-1):
                    odd_count_subset.append(max(count_odd))
       
        if(len(count_odd)==0):
            return sum(count_even)
    
        elif (len(count_even) == 0):
            return max(count_odd) + sum(odd_count_subset) - len(odd_count_subset)
        else:
            return sum(count_even) + max(count_odd) + sum(odd_count_subset) - len(odd_count_subset)
            