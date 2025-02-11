class Solution:
    def frequencySort(self, s: str) -> str:
        chars_count = Counter(s)

 
        chars_count = dict(sorted(chars_count.items(), reverse = True, key = lambda x : x[1]))

        results = []
        for char in chars_count:
            while chars_count[char] > 0:
                results.append(char)
                chars_count[char] -= 1

        return "".join(results)

        