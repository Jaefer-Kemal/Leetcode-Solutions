class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0 for _ in range(1001)]
        for t in trips:
            stops[t[1]] += t[0]
            stops[t[2]] -= t[0]
        
        for i in range(1001):
            capacity -= stops[i]
            if capacity < 0:
                return False
        
        return capacity >= 0
        
        
#         dic = {}
#         maxim = float("-inf")
#         for i in range(len(trips)):
            
#             for j in range(trips[i][1],trips[i][2]):
#                 if j not in dic:
#                     dic [j] = trips[i][0]
#                 else:
#                     dic [j] += trips[i][0]
#                 print(maxim)
#                 if maxim < dic[j]:
#                     maxim = dic[j]
#                     if maxim > capacity:
#                         return False
                    
#         if maxim > capacity:
#             return False
#         return True
                    