from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = [int(x) for x in range(1,n+1)]
        d = deque(arr)
        count = 1
        
        while len(d) != 1:
            
            if count % k == 0:
                d.popleft()
            else:
                d.append(d[0])
                d.popleft()
            
            count += 1
        
        return d[0]
                
        
        
        
        
'''The First solution'''
        
#         out =  set()
#         count = 1
        
#         for i in range(n*100000000):
#             num = arr[i % n]
            
#             if (len(out) == n-1) and (num not in out):
#                 print(num)
#                 return num
            
#             if count % k == 0 and len(out) != n-1:
#                 if num not in out:
#                     out.add(num)
#                     count += 1
            
#             if num not in out:
#                 count += 1
                
                
        