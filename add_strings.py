"""
Think of how you would add two numbers on paper, manually.
1. You start from the end (right side) of the two strings
2. You keep track of the carry

"""




class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)>5100 or len(num2)>5100:
            return None
        
        # can I use int() on length 1 strings? seems impossible
        # without using int() tbh.
        
        # ugh. I'll come back to this later. I am tired now.
        carry = 0
        result = []
        i, j = len(num1) - 1, len(num2) - 1 # pointers to the end of both numbers
        while i>=0 or j>=0:
            sum_ = carry
            if i>=0:
                sum_ += int(num1[i])
                i -= 1
            if j>=0:
                sum_ += int(num2[j])
                j -= 1
                
            result.append(str(sum_%10))
            carry = sum_//10
            
        if carry != 0:
            result.append(str(carry))
        return ''.join(result[::-1])
            