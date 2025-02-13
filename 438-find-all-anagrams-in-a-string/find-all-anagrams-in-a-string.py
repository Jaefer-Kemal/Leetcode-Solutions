class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_chars_count = Counter(p)
        k = len(p)
        s_chars_count = Counter(s[:k])

        anagram_index = []
        if p_chars_count == s_chars_count:
            anagram_index.append(0)

        left = 0
        for right in range(k,len(s)):
            s_chars_count[s[right]] += 1
            s_chars_count[s[left]] -= 1

            if s_chars_count[s[left]] <= 0:
                del s_chars_count[s[left]]
            
            left += 1

            if s_chars_count == p_chars_count:
                anagram_index.append(left)
        
        return anagram_index

        