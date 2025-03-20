class Solution:
    
    def longestNiceSubstring(self, s: str) -> str:
        exist = set(s)
        unwanted = []

        for i, char in enumerate(s):
            if not(char.lower() in exist and char.upper() in exist):
                unwanted.append(i)
        
        if len(unwanted) == 0:
            return s

        if len(unwanted) == len(s):
            return ""

        result = ""
        
        for i, index in enumerate(unwanted):
            if i==0:
                word = (self.longestNiceSubstring(s[:index]))
                if result:
                    if len(result) < len(word):
                        result = word
                else:
                    result = word
            else:
                word = (self.longestNiceSubstring(s[unwanted[i-1]+1: index]))

                if result:
                    if len(result) < len(word):
                        result = word
                else:
                    result = word

        word = (self.longestNiceSubstring(s[unwanted[-1]+1:]))

        if result:
            if len(result) < len(word):
                result = word
        else:
            result = word

        return result 