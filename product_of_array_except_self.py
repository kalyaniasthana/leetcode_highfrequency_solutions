"""
the first solution which came to my mind was, obviously, you guessed it,
take the product of all the elements and divide and by the element at index[i]
for the final answer.
I had to look at the solution algorithm for this one. didn't look at the code though. 
should avoid doing that as much as possible.

key to the solution is to think about maintaining two array- one with all left
products and one with all right products. later, modify this approach(for better
space complexity) by maintaining either one of the left or right product arrays
and use a running product for the other one.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array =  [1]
        right_array = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            left_array.append(nums[i-1]*left_array[i-1])
        # for i in range(len(nums)-2, -1, -1):
        #     right_array[i] = nums[i+1]*right_array[i+1]
        # for i in range(len(nums)):
            # nums[i] = left_array[i]*right_array[i]
        # return nums
        # ok so this works
        # how do I do this in constant space complexity?!
        # damn this is hard
        right_product = 1
        print(left_array)
        for i in range(len(nums) - 1, -1, -1):
            print(right_product)
            temp = nums[i]
            nums[i] = right_product*left_array[i]
            right_product = right_product*temp
        return nums
        