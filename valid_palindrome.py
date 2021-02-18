"""
Make sure you use str.isalnum() and not str.isalpha(). READ THE QUESTION CAREFULLY.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphanumeric characters from the string
        new_string = ""
        s = s.lower()
        for i in range(len(s)):
            if not s[i].isalnum():
                continue
            new_string += s[i]
        i, j = 0, len(new_string)-1
        while(i<=j):
            if new_string[i] !=new_string[j]:
                return False
            i+=1
            j-=1
        return True

            