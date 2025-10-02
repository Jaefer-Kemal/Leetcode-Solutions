class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if len(word_list) != len(pattern):
            return False

        memo = {}
        visited = set()
        for i in range(len(pattern)):
            if pattern[i] not in memo:
                if word_list[i] in visited:
                    return False
                memo[pattern[i]] = word_list[i]
                visited.add(word_list[i])

            elif memo[pattern[i]] != word_list[i]:
                    return False
        
        return True


        

        