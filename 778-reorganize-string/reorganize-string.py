class Solution:
    def reorganizeString(self, s: str) -> str:
        chars_count = defaultdict(int)
        max_char = ""
        max_count = 0

        for char in s:
            chars_count[char] += 1
            if max_count < chars_count[char]:
                max_char = char
                max_count = chars_count[char]
        
        if (chars_count[max_char] > (len(s) + 1) // 2):
            return ""
        
        res = [""] * len(s)

        i = 0
        while (chars_count[max_char]):
            res[i] = max_char
            chars_count[max_char] -= 1
            i += 2

        for index in range(27):
            char = chr(ord('a') + index)
            while(chars_count[char]):
                if i >= len(res):
                    i = 1

                res[i] = char
                i += 2
                chars_count[char] -= 1
        
        return "".join(res)
        