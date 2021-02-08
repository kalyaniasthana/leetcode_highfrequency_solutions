""" Thoughts? 
Alright so TBH solving this took me quite some time. 
When I read the question I instantly knew that I 
have to use a dictionary(hash map). After my first implementation
using a dictionary I saw one problem. What was this problem? 
How the hell I am going to take care of inputs with multiple 
equal values (for example: [3, 3], target = 6). 
After toiling for some time I realised that the key to the
solutions is to iterate over the input list and create the 
dictionary at the same time.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        l = []
        for i in range(len(nums)):
            current_num = nums[i]
            if (target - nums[i]) in hash_map:
                return [hash_map[target - nums[i]], i]
            hash_map[nums[i]] = i

