class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars_count = Counter(s)
        longest = 0
        isOdd = False

        for char in chars_count:
            value = chars_count[char]
            longest += (value // 2) * 2
            if not isOdd:
                if value % 2 != 0:
                    longest += 1
                    isOdd = True
        
        return longest
            
        
        