class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # solution this problem is called - Kandane's Algorithm
        # remember that we don't need to return the 
        # subarray. we only need to  return the
        # maximum sum value of any subarray with 
        # >= 1 elements.
        
        # first come up with a crappy brute force solution
        # let's look at all subarrays - check their sums
        # O(n**2) super slow
        '''
        max_sum = float('-Inf')
        current_sum = 0
        N = len(nums)
        for i in range(N):
            current_sum = nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            for j in range(i+1, N):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
        '''
        # can you come up with a linear run time solution
        # HELL YES
        # iterate through the list
        # find maximum sum upto element i
        # figure out whether the next element should be added 
        # to this sum OR to start a new sum
        max_sum = nums[0]
        current_sum = max_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i] + current_sum, nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum
        
                
            