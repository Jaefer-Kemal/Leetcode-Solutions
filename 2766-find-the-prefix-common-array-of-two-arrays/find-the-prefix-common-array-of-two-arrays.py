class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        common = set()
        res = []

        for i in range(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            
            res.append(len(setA & setB))
        
        return res


        