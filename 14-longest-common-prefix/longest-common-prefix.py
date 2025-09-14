class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = strs[0]

        for word in strs:
            if len(min_str) > len(word):
                min_str = word
        
        res = []
        for char in range(len(min_str)):
            for word in strs:
                if word[char] != min_str[char]:
                    return "".join(res)
            
            res.append(min_str[char])
        
        return "".join(res)

                
