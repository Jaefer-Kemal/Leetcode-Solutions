class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_chars = Counter(text)
        occurrence = float('inf')

        for char in 'balon':
            if char == "o" or char == "l":
                cnt = count_chars[char] // 2
            else:
                cnt = count_chars[char]

            if occurrence > cnt:
                occurrence = cnt
                    
        return occurrence
        