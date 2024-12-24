class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        check = Counter(s)
        for char in t:
            if char not in check:
                return char
            else:
                check[char] -= 1
                if check[char] == 0:
                    del check[char]
        