"""
pretty easy. just need to be careful with the if elif else conditions. 
don't miss any. 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        
        for i in range(len(s)):
            # print(stack)
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' and len(stack)!=0 and stack[-1]=='(':
                stack.pop(-1)
            elif s[i]=='}' and len(stack)!=0 and stack[-1]=='{':
                stack.pop(-1)
            elif s[i]==']' and len(stack)!=0 and stack[-1]=='[':
                stack.pop(-1)
            else:
                """If any of the above conditions are not met
                then we instantly know that something is wrong. 
                Like in this example: ([}}])
                """
                return False
        return len(stack)==0