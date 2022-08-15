# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Explanation:

# First find the shortest string in the list, call it prefix. That is our temporary prefix.
# Iterate through every element in strs:
# while the prefix doesn't match the prefix (first len(prefix) character) of the element,
# remove the last character from prefix.
# After iterations, return prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs, key=len)
        for i in strs:
            while prefix != i[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) ==1:
#             return strs[0]
#         strs.sort()
#         print(strs)
#         ans=""
#         count=0
#         flag=0
#         for i in range(1,len(strs[0])):
            
#                if flag==1:
#                     return ans
#                s=strs[0]
#                for j in range(1,len(strs)):
#                     if s[0] != strs[j][0]:
#                         count+=1
#                     else:
#                         pass
#                     if count== len(strs)-1:
#                         return ""
#                     print("ans= ",ans)
#                     print("s[:i] "+s[:i]+" strs[j] "+strs[j])
#                     if s[:i] != strs[j][:i]:
#                         flag=1
#                     else:
#                         ans=s[:i]                            
                       
#         return ans
