class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        last_ind = len(arr)

        res = []
        while last_ind != 1:
            max_ind = 0
            for i in range(last_ind):
                if arr[i] > arr[max_ind]:
                    max_ind = i
            res.append(max_ind + 1)
            
            arr = list(reversed(arr[0:max_ind + 1])) + arr[max_ind + 1:]
            arr = list(reversed(arr[0 : last_ind])) + arr[last_ind : ]

            res.append(last_ind)
            last_ind -= 1

        return res