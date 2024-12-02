class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []
        s = list(s)

        for char in s:
            if char.lower() in ['a', 'e', 'i', 'o','u']:
                vowel.append(char)
    

        l = 1
        for idx, char in enumerate(s):
            if char.lower() in ['a', 'e', 'i', 'o','u']:
                s[idx] = vowel[-l]
                l += 1

        return "".join(s)

