class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        set_string = set()
        res = 0

        for word in words:
            if word[::-1] in set_string:
                res += 1
            else: set_string.add(word)
        
        return res
