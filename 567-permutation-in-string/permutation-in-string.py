class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        test = [0] * 26
        for char in s1:
            test[ord(char) - ord("a")] += 1

        check = [0] * 26
        for r in range(len(s1)):
            check[ord(s2[r]) - ord("a")] += 1
        
        if check == test:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            check[ord(s2[r]) - ord("a")] += 1
            check[ord(s2[l]) - ord("a")] -= 1

            if check == test:
                return True
            l += 1
        return False

            
            