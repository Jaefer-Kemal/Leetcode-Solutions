class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 1
        arr = [int(x) for x in range(1,n+1)]
        out =  set()
        
        
        for i in range(n*100000000):
            num = arr[i % n]
            
            if (len(out) == n-1) and (num not in out):
                print(num)
                return num
            
            if count % k == 0 and len(out) != n-1:
                if num not in out:
                    out.add(num)
                    count += 1
            
            if num not in out:
                count += 1
                
                
        