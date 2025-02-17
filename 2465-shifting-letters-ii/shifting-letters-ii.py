class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s) 
        prefix = [0] * (n + 2)
        
        for start, end, direction in shifts:
            if direction:
                steps = 1
            else:
                steps = -1

            prefix[start] += steps
            prefix[end + 1] -= steps
        
        for i in range(1, n + 2):
            prefix[i] += prefix[i - 1]
        
        final_string = [0] * n
        for i in range(n):
            updated_char = (ord(s[i]) - ord("a"))  + prefix[i]
            updated_char = chr((updated_char % 26) + ord("a"))

            final_string[i] = updated_char
        
        return "".join(final_string)

            