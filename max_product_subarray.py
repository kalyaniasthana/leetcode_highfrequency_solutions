class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # let's do brute force first
        '''
        max_prod, current_prod = 0, 0
        for i in range(len(nums)):
            current_prod = nums[i]
            max_prod = max(max_prod, current_prod)
            for j in range(i+1, len(nums)):
                current_prod *= nums[j]
                max_prod = max(max_prod, current_prod)
        return max_prod
        '''
        max_prod, curr_min, curr_max = max(nums), 1, 1
        # trick -> also keep track of the minimum subarray prod
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_min, curr_max = 1, 1
                continue
            # declaring this temp variable since the value of curr_max
            # changes at the next step, but we need the old value at the
            # next to next step
            temp = nums[i]*curr_max
            # current max subarray product
            curr_max = max(temp, nums[i]*curr_min, nums[i])
            # current min subarray product
            curr_min = min(temp, nums[i]*curr_min, nums[i])
            # max product 
            max_prod = max(max_prod, curr_max)
        return max_prod
                
        
                