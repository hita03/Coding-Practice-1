// Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "cbaebabacd", p = "abc"
// Output: [0,6]
// Explanation:
// The substring with start index = 0 is "cba", which is an anagram of "abc".
// The substring with start index = 6 is "bac", which is an anagram of "abc".
// Example 2:

// Input: s = "abab", p = "ab"
// Output: [0,1,2]
// Explanation:
// The substring with start index = 0 is "ab", which is an anagram of "ab".
// The substring with start index = 1 is "ba", which is an anagram of "ab".
// The substring with start index = 2 is "ab", which is an anagram of "ab".
 



// class Solution(object):
//     def checkAnagram(self,s,p,l):
//         s_d={}
//         p_d={}
//         for i in range(len(s)):
//             if s[i] not in s_d:
//                 s_d[s[i]] = 1;
//             elif s[i] in s_d:
//                 s_d[s[i]] += 1; 
            
//             if p[i] not in p_d:
//                 p_d[p[i]] = 1;
//             elif p[i] in p_d:
//                 p_d[p[i]] += 1; 
//         if p_d.keys() == s_d.keys() and p_d.values() == s_d.values():
//             return True
//         return False
        
        
//     def findAnagrams(self, s, p):
//         res = []
//         n=len(s)
//         l=len(p)
//         i=0
//         for i in range(n):
//             if i+l <= n: 
//                 if p == s[i:l+i] or self.checkAnagram(s[i:l+i],p,l):
//                     res.append(i)            
                
//         return res    
        



// class Solution(object):
//     def checkFreq(self,char,s):
//         c=0
//         for ch in s:
//             if char == ch:
//                 c+=1
//         return c        
        
//     def checkAnagram(self,s,p,l):
//         x=0
//         for i in range(len(s)):
//             if self.checkFreq(s[i],p) != 0:
//                 if self.checkFreq(p[i],s) == self.checkFreq(p[i],p):
//                     x+=1
//         if x == l:
//             return True
//         return False
        
//     def findAnagrams(self, s, p):
//         res = []
//         n=len(s)
//         l=len(p)
//         i=0
//         for i in range(n):
//             if i+l <= n: 
//                 if self.checkAnagram(s[i:l+i],p,l):
//                     res.append(i)            
                
//         return res    
                

from collections import Counter

class Solution(object):
  
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res                