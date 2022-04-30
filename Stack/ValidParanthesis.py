# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        for i in range(len(s)):
            if s[i] == '(' or  s[i] == '{' or  s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')' or  s[i] == '}' or  s[i] == ']':  
                    if not len(stack) == 0:
                        peek = stack[len(stack)-1]
                        if peek == '(' and s[i] == ')' or peek == '[' and s[i] == ']' or peek == '{' and s[i] == '}':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                    
        if len(stack) == 0:
            return True
                        
                
        