class Solution:
    def maxFreqSum(self, s: str) -> int:
        chars_count = Counter(s)
        vowels = {"a","e","i","o","u"}
        maximum_vowel = 0
        maximum_consonant = 0

        for char in chars_count:
            freq = chars_count[char]
            if char in vowels:
                if maximum_vowel < freq:
                    maximum_vowel = freq

            elif maximum_consonant < freq:
                maximum_consonant = freq
        
        return maximum_consonant + maximum_vowel

        