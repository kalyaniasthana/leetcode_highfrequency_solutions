class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # how the hell do I do this without using a third list? 
        # alright, seems like my intuition was correct. you can't
        # solve this problems w/o allocating a third array
        # ahh why isn't this working? we're almost there
        nums3 = nums1[:m] # copy of nums1 non empty elements 
        i, j = 0, 0 # pointers to nums3 and nums2 respectively
        for k in range(m+n):
            if j>=n or (i<m and nums3[i] <= nums2[j]): # if you've already traversed nums2 OR if nums3 has the smaller element
                nums1[k] = nums3[i]
                i += 1
            else:
                nums1[k] = nums2[j] # includes cases where i>=m AND where nums2 has the smaller element
                j += 1
            
            
                
        