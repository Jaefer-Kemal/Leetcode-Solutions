class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        string_count = defaultdict(int)
        cnt = 1
        for s in arr:
            string_count[s] += 1
        

        for string in string_count:
            if string_count[string] == 1:
                if cnt == k:
                    return string
                cnt += 1
        
        return ""
        