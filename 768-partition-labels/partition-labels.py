class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # We will count all the characters frequency
        chars_count = Counter(s)
        # The result that we are going to return
        partition_sizes = []
        # checking characters that will be included as part
        current_partition = defaultdict(int)
        # If we manage to collect every character in the current partition
        # and their frequency match with the char:frequency in the chars_count
        # we will append that specific character
        completed_chars = set()
        left = 0
        for right in range(len(s)):

            current_partition[s[right]] += 1
            # if the frequncy of character matches then that mean
            # we are sure that this specific character wont be appearing
            # in another partitions
            if current_partition[s[right]] == chars_count[s[right]]:
                completed_chars.add(s[right])
            # If we manage to have those character appearing only in this partition
            # then we have fullfilled the condition for this part
            # and we will create another partition and repeat the same process
            if completed_chars and len(completed_chars) == len(current_partition):
                partition_sizes.append(right - left + 1)
                left = right + 1
                completed_chars = set()
                current_partition = defaultdict(int)

        return partition_sizes
