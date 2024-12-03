class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord("a")] += 1
                
            freq = tuple(freq)
            cnt[freq].append(s)
           
        return list(cnt.values())
            
            


        