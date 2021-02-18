"""
Trick is to have a normal stack
and a stack with just the minimum elements
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_vals = []
        current_min = float('Inf')      

    def push(self, x: int) -> None:
        if len(self.min_vals)==0 or x<=self.min_vals[-1]:
            self.min_vals.append(x)
            # print(self.min_vals, 'mv')
        self.stack.append(x)
        # print(self.stack, 'stack')

    def pop(self) -> None:
        if len(self.stack)>0:
            if self.stack[-1]==self.min_vals[-1]:
                self.min_vals.pop(-1)
            self.stack.pop(-1)

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]     

    def getMin(self) -> int:
        return self.min_vals[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()