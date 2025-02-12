class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_piles = 0
        piles.sort()
        i = 0
        j = len(piles)
        while j - i >= 3:
            # Alice pile since she always pick the maximum number of coins
            piles.pop()
            j -= 1
            # I will pick second maximum number of coins after Alice
            my_piles += piles.pop()
            j -= 1
            # Bob will pick the smallest number of coins
            i += 1

        return my_piles

        