class Solution:
    
    def longestNiceSubstring(self, s: str) -> str:

        def divide_and_conquer(s):
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
                    x = (divide_and_conquer(s[:index]))
                    if result:
                        if len(result) < len(x):
                            result = x
                    else:
                        result = x
                else:
                    x = (divide_and_conquer(s[unwanted[i-1]+1: index]))
                    if result:
                        if len(result) < len(x):
                            result = x
                    else:
                        result = x
            x = (divide_and_conquer(s[unwanted[-1]+1:]))
            if result:
                if len(result) < len(x):
                    result = x
            else:
                result = x
            print(result)
            return result
    
        return divide_and_conquer(s)
        