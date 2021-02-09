"""
Um.. why is this problem considered 'easy'? and why are some of the 
'medium' problems actually super hard?!
Anyway, this took me very long. Probably around 1.5 hours. It was super-
not-straightforward.
How to approach this problem? Honestly, I just couldn't think. I tried.
https://www.youtube.com/watch?v=qSbJZWENtX4 -> this helped me. this guys works for algoexpert now. 
amazing.


VV IMP - remember to make a separate function for comparing pair of strings. Keeps
the code clean.
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    
        alphabet_order = {order[i]: i for i in range(len(list(order)))}
        
        def compare(word1, word2):
            char_compare = 0
            i, j = 0, 0
            while (i < len(word1) and j < len(word2) and char_compare == 0):
                char_compare = alphabet_order[word1[i]] - alphabet_order[word2[j]]
                i += 1
                j += 1
            
            if char_compare == 0:
                return len(word1) - len(word2) # takes care of words with similar prefixes
            else:
                return char_compare # takes care of totally different words 
            # alright now this makes total sense
            
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i+1]
            if compare(first_word, second_word) > 0:
                return False
        return True
            