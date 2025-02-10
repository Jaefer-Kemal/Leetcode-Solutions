class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maximum = max(arr1) + 1
        range_arr = [0] * maximum
        for num in arr1:
            range_arr[num] += 1
        
        visited = set()
        res = []
        for num in arr2:
            count = range_arr[num]
            while count > 0:
                res.append(num)
                count -= 1
            visited.add(num)
        
        for num in range(maximum):
            if num not in visited:
                count = range_arr[num]
                while count > 0:
                    res.append(num)
                    count -= 1
        
        return res
        