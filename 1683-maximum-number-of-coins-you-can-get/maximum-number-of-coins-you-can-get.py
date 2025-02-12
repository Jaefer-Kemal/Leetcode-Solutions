class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_piles = 0
        piles = deque(sorted(piles))
        while len(piles) >= 3:
            # Alice pile since she always pick the maximum number of coins
            piles.pop()
            # I will pick second maximum number of coins after Alice
            my_piles += piles.pop()
            # Bob will pick the smallest number of coins
            piles.popleft()

        return my_piles

        