class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        iso1 = {}
        iso2 = {}

        for index in range(len(s)):
            char1 = s[index]
            char2 = t[index]

            if (char1 not in iso1) and (char2 not in iso2):
                iso1[char1] = char2
                iso2[char2] = char1
            
            elif (char1 not in iso1 and char2 in iso2) or (char2 not in iso2 and char1 in iso1):
                return False
                
            elif iso1[char1] != t[index] or iso2[char2] != s[index]:
                    return False
        
        return True
        