# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

class Solution(object):
    def getFreq(self, d, s):
        for i in s:
            if i not in d:
                d[i] = 1;
            else:
                d[i]+=1;
        return d;
    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        b = 0
        c = 0
        sd = self.getFreq({}, secret)
        gd = self.getFreq({}, guess)
        # print(sd,gd)
        for i in range(len(guess)):
            # print(guess[i],secret[i], guess[i] in secret)
            if guess[i] == secret[i]:
                sd[secret[i]]-=1
                gd[secret[i]]-=1
                b+=1
        for k in sd:
            if k in gd:
                print(sd[k], gd[k],k)
                c += min(sd[k], gd[k])          
        return "{x}A{y}B".format(x=b,y=c)            