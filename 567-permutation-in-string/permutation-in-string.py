class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)
        s1_chars_count = Counter(s1)
        # create a counter until the length of string s1
        window = Counter(s2[:window_size])

        if window == s1_chars_count:
            return True
        
        left = 0
        for right in range(window_size, len(s2)):
            # include the next character into the window
            window[s2[right]] += 1
            # remove the leftmost charater from the window
            window[s2[left]] -= 1
            
            # if frequency of character is zero, then we can simple delete the key
            if window[s2[left]] == 0:
                del window[s2[left]]
            
            left += 1

            if window == s1_chars_count:
                return True
        
        return False
        
        