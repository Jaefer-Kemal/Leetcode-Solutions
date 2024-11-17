class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = {}
        maxim = float("-inf")
        for i in range(len(trips)):
            
            for j in range(trips[i][1],trips[i][2]):
                if j not in dic:
                    dic [j] = trips[i][0]
                else:
                    dic [j] += trips[i][0]
                print(maxim)
                if maxim < dic[j]:
                    maxim = dic[j]
                    if maxim > capacity:
                        return False
                    
        if maxim > capacity:
            return False
        return True
                    