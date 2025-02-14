class Solution:
    def minWindow(self, s: str, t: str) -> str:

        target = Counter(t)

        min_length = float("inf")
        l = 0
        minimum_window = ""

        completed_chars =set()
        s_chars_count = defaultdict(int)
        
        left = 0
        for right in range(len(s)):
            s_chars_count[s[right]] += 1

            if s_chars_count[s[right]] == target[s[right]]:
                completed_chars.add(s[right])
            
            while len(target) == len(completed_chars):
                if min_length > right - left + 1:
                    min_length = right -  left + 1
                    l = left 
                
                s_chars_count[s[left]] -= 1
                if s[left] in target and s_chars_count[s[left]] < target[s[left]]:
                    completed_chars.discard(s[left])

                left += 1


        return "" if min_length == float("inf") else s[l: l + min_length]