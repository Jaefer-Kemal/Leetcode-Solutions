class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = {}
        for s in strs:
            ls = [0] * 26
            for char in s:
                ls[ord(char) - ord("a")] += 1
                
            ls = tuple(ls)
            if ls not in cnt:
                cnt[ls] = [s]
            else:
                cnt[ls].append(s)
        res = []   
        
        for val in cnt.values():
            res.append(val)
        return res
            
            


        