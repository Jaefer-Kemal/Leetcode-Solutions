class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = {'a', 'e', 'i', 'o','u', "A", "E", "I", "O", "U"}
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].lower() not in vowel:
                l += 1
            elif s[r].lower() not in vowel:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                

        return "".join(s)

