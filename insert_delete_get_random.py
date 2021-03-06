"""
lol, totally not a medium level problem. this was too easy.
"""


import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        self.map = {}     

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.map:
            self.set.append(val)
            self.map[val] = None
            return True
        return False
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.map:
            self.set.remove(val)
            del self.map[val]
            return True
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()