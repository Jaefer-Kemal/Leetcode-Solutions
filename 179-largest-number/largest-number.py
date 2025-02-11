class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str,nums))

        # Sort numbers based on their concatenated value
        # We multiply each string by 10 to ensure consistent lexicographical comparison like "3" -> "3333333333" and "30" -> "30303030303030" 
        # since its lexigraohical comparison it doesnt matter the length of the string.
        str_nums.sort(key = lambda x: x * 10, reverse = True)

        res = "".join(str_nums)
        if res[0] == "0":
            return "0"
        else:
            return res