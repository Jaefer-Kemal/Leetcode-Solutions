class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = defaultdict(set)
        trusted = set()

        for a, b in trust:
            trusted_by[b].add(a)
            trusted.add(a)
        
        for node in range(1, n + 1):
            if len(trusted_by[node]) == n - 1 and node not in trusted:
                return node
        
        return -1