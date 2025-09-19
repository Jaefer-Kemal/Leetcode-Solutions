import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_indexes = defaultdict(list)
        res = 0

        for index, char in enumerate(s):
            char_indexes[char].append(index)
        
        for word in words:
            index = float('-inf')
            
            for char in word:
                pos_list = char_indexes[char]
                j = bisect.bisect_right(pos_list, index)
                if j >= len(pos_list):
                    break
                index = pos_list[j]

            else:
                res += 1
        
        return res