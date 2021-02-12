"""
This is super easy. Makes me want to rethink my solution for the Reverse Integer Problem.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<-2**31 or x>2**31-1:
            return False
        if (x<0) or (x>0 and x%10==0):
            return False
        temp = x
        reverse = 0
        while temp!=0:
            reverse = reverse*10 + temp%10
            temp=temp//10
        return reverse==x