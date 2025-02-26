class Solution:
    def equalFrequency(self, word: str) -> bool:
        chars_count = Counter(word)
        temp = chars_count.copy()

        for char in chars_count:
            temp[char] -= 1
            if temp[char] == 0:
                del temp[char]

            if len(set(temp.values())) == 1:
                return True
            
            temp[char] += 1
        
        return False