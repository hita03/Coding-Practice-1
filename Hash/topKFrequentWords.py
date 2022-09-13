# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         count = {}
#         freq =[[] for i in range(len(words)+1)]
        
#         for n in words:
#             count[n] = 1+ count.get(n,0)
        
#         for n,c in count.items():
#             freq[c].append(n)
            
#         res = []
#         # desc order for most frequent
#         for i in range(len(freq)-1,0,-1):
#             for n in freq[i]:
#                 if len(res) == k:
#                     break
#                 res.append(n)
#         return  res      
        
        d = collections.defaultdict(int)
        for word in words:
            d[word] += 1
        bucket = [[] for _ in range(len(words) + 1)]
        for key in d:
            bucket[d[key]].append(key)
        res = []
        for i in reversed(range(len(words) + 1)):
            if len(res) >= k:
                break
            if len(bucket[i]) > 0:
                bucket[i].sort()
                if len(bucket[i]) + len(res) <= k:
                    res += bucket[i]
                else:
                    res += bucket[i][:k - len(res)]
        return res