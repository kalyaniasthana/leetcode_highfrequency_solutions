
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

"""
Realised after a few days that the above solution is overly complicated.
I got something better now.

"""

class Solution:
    def reverse(self, x: int) -> int:
        if x%10 == x: # single digit number
            return x 
        if x < -2**31 or x > 2**31-1:
            return 0
        
        reverse = 0
        sign = 1 if x>0 else -1
        x = abs(x)
        temp = x
        
        while temp!=0:
            reverse = reverse*10 + temp%10
            temp=temp//10
            
        reverse = sign*reverse
        if reverse < -2**31 or reverse > 2**31-1:
            return 0
        
        return reverse
    
    
    
    
        