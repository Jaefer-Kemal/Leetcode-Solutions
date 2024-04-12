class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        given=Counter(s1)
        r=0
        while r<len(s2):
            checked=Counter(s2[r:r+k])
            if given == checked:
                return True
            r+=1
        return False


            
        