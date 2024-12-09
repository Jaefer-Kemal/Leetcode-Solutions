class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = deque()

        for num in arr:
            if res:
                if k == 0:
                    if res[0] == num:
                        continue
                    elif abs(res[0] - x) > abs(num - x):
                        res.popleft()
                        res.append(num)
                    else:
                        break
                else:
                    res.append(num)
                    k -= 1
                    
            else:
                res.append(num)
                k -= 1

        return list(res)
        