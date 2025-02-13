class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars_count = Counter(s)
        results = []
        fullfilled_set = set()
        part_dict = defaultdict(int)
        left = 0
        for right in range(len(s)):
            part_dict[s[right]] += 1
            if part_dict[s[right]] == chars_count[s[right]]:
                fullfilled_set.add(s[right])
            
            if fullfilled_set and len(fullfilled_set) == len(part_dict):
                print(s[left:right])
                results.append(right - left + 1)
                left = right + 1
                fullfilled_set = set()
                part_dict = defaultdict(int)

        return results
