class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram_checker = set()
        for char in sentence:
            pangram_checker.add(char)
        
        if len(pangram_checker) >= 26:
            return True
        
        return False
