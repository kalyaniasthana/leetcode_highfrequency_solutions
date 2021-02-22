"""
use hash map to keep track of cummulative sum

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force -> iterate through all subarrays O(n**2)
        cumsum, result = 0, 0
        # hash map for all cummulative sums
        arr_sums = {0: 1} 
        
        for i in range(len(nums)):
            # keeping a track of the cummulative sum
            cumsum += nums[i]
            
            # if we have seen cumsum-k before then it implies that
            # the sum between the current element that the cumsum 
            # the previous point is k
            if (cumsum-k) in arr_sums:
                result += arr_sums[cumsum-k]
            
            #if cumsum is already in arr_sums
            if cumsum in arr_sums:
                arr_sums[cumsum] += 1
            else:
                arr_sums[cumsum] = 1
                
        return result