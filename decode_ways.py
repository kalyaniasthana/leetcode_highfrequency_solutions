"""Super Important Question: thank you csdojo for the best
explanation video ever
"""
# Solution 1: only recursion
# slow for inputs like """11111111111""" - O(2**n) -> think of the recursion tree to derive complexity
class Solution:

	def helper(self, data, k):
		# base case 1
		if k == 0:
			return 1

		# base case 2
		s = len(data) - k
		if data[s] == '0':
			return 0

		result = self.helper(data, k-1)
		if k>=2 and int(data[s:s+2])>=26:
			result += self.helper(data, k-2)
		return result
        
    def numDecodings(self, s: str) -> int:
    	return self.helper(s, len(s))


# Solution 2: dp + recursion 
# O(n)
# using memo to somehow store the no. of way to decide any substring part of the main input string
class Solution:

	def helper(self, data, k, memo):
		# base case 1
		if k == 0:
			return 1

		# base case 2
		s = len(data) - k
		if data[s] == '0':
			return 0

		if memo[k] is not None:
			return memo[k]

		result = self.helper(data, k-1, memo)
		if k>=2 and int(data[s:s+2])>=26:
			result += self.helper(data, k-2, memo)
		memo[k] = result
		return result
        
    def numDecodings(self, s: str) -> int:
    	memo = [None for i in range(len(s) + 1)]
    	return self.helper(s, len(s), memo)
    	