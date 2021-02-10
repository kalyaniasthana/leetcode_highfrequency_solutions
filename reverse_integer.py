
"""
Meh. this was too easy. but fun to solve.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x%10 == x:
            return x 
        l = []
        sign = 1 if x>0 else -1
        x = abs(x)
        temp = x
        steps = 0
        while True:
            steps += 1
            l.append(temp%10)
            temp //=10
            if temp < 10:
                l.append(temp)
                break
        for i in range(len(l)):
            l[i] *= 10**steps
            steps -= 1
            if steps < 0:
                break
        final_x = sign*sum(l)
        if final_x < -2**31 or final_x > 2**31-1:
            return 0
        return final_x
    
    
        