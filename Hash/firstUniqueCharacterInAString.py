# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=s
#         li=[]
#         for i in range(len(temp)-1):
#             for j in range(i+1,len(temp)):
#                 if temp[i] == temp[j]:
#                     # print(i)
#                     li.append(temp[j])
#                     break;        
        
#         for i in range(len(temp)):
#             if temp[i] not in li:
#                 print(temp[i])
#                 return i

#         return -1

        d={}
        for i in range(26):
            d[chr(i+97)]=0
        # print(d)
        for l in s:
            if l not in d:
                d[l]=1
            else:
                d[l]+=1


        print(d)
        for i in range(len(s)):

            if d[s[i]]==1:
                
                return i
                # break

        # print(index)
        return -1

        