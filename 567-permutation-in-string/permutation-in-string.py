class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        test = Counter(s1)
        check = Counter()
        if len(s2) < len(s1):
            return False
            
        for r in range(len(s1)):
            check[s2[r]] += 1
        
        if check == test:
            return True

        l = 0
        for r in range(len(s1),len(s2)):
            check[s2[r]] += 1
            check[s2[l]] -= 1
            print(check)
            if check == test:
                return True
            l += 1
        return False

            
            