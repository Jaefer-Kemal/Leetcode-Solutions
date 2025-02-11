class Solution:
    def frequencySort(self, s: str) -> str:
        chars_count = Counter(s)

        helpers = []
        for char in s:
            helpers.append([char, chars_count[char]])

        helpers.sort(reverse = True, key = lambda x : (x[1], x[0]))

        results = []
        for index in range(len(helpers)):
            results.append(helpers[index][0])

        return "".join(results)

        