class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        distinct_broken_key = set(brokenLetters)
        split_text = text.split(" ")
        res = 0

        for word in split_text:
            for char in word:
                if char in distinct_broken_key:
                    res -= 1
                    break
        
            res += 1
        
        return res
                

        