'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

# class Solution(object):
    
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         n =len(s)
#         maxLength=0
#         table=[[0 for i in range(n)] for j in range(n)]
        
#         print(s)

        
#         for i in range(n):
#             table[i][i]=1 #lt 1 substring is always palindrome
            
#         #checking for substring 2 palindrome. only for aa,bb,xx type is palindrome
#         start = 0
#         i = 0
#         while i < n - 1 :
#             if (s[i] == s[i + 1]) :
#                 table[i][i + 1] = 1
#                 start = i
#                 maxLength = 2
#             i = i + 1 
            
#         k=3   
#         while k<=n:

#             i=0
#             while i< (n-k+1):
#                 # Get the ending index of
#                 # substring from starting
#                 # index i and length k
#                 j=i+k-1


#                 # checking for sub-string from
#                 # ith index to jth index iff
#                 # st[i + 1] to st[(j-1)] is a
#                 # palindrome  

#                 if (table[i + 1][j - 1] and s[i] == s[j]) :
#                     table[i][j] = 1


#                 if (k > maxLength) :
#                     start = i
#                     maxLength = k
#                 i = i + 1
#         return s[start: maxLength-1]

# Python program


class Solution(object):
    
    def longestPalindrome(self, s):
        n = len(s) # get length of input string

        # table[i][j] will be false if substring
        # str[i..j] is not palindrome. Else
        # table[i][j] will be true
        table = [[0 for x in range(n)] for y
                            in range(n)]

        # All substrings of length 1 are
        # palindromes
        maxLength = 1
        i = 0
        while (i < n) :
            table[i][i] = True
            i = i + 1

        # check for sub-string of length 2.
        start = 0
        i = 0
        while i < n - 1 :
            if (s[i] == s[i + 1]) :
                table[i][i + 1] = True
                start = i
                maxLength = 2
            i = i + 1

        # Check for lengths greater than 2.
        # k is length of substring
        k = 3
        while k <= n :
            # Fix the starting index
            i = 0
            while i < (n - k + 1) :

                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1

                # checking for sub-string from
                # ith index to jth index iff
                # st[i + 1] to st[(j-1)] is a
                # palindrome
                if (table[i + 1][j - 1] and
                        s[i] == s[j]) :
                    table[i][j] = True

                    if (k > maxLength) :
                        start = i
                        maxLength = k
                i = i + 1
            k = k + 1


        return s[start: maxLength] # return length of LPS


