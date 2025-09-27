class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        res = []

        for participant in order:
            if participant in friends_set:
                res.append(participant)
        
        return res
        