class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        uni=[set(word) for word in words]
        uni.sort(key=len)
        l=0
        r=l+1
        res=0
        while l<len(uni) and r<len(uni):
            n=len(uni[l])
            if n==len(uni[r]):
                if uni[l]==uni[r]:
                    res+=1
                    r+=1
                else:
                    r+=1
            else:
                l+=1
                r=l+1
            if r==len(uni):
                l+=1
                r=l+1
        print(uni)
        return res

        