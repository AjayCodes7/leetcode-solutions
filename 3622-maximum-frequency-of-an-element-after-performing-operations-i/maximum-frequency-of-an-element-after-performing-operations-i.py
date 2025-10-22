class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        frequency = defaultdict(int)
        difference = defaultdict(int)
        for num in nums:
            frequency[num] += 1
            difference[num] += 0

            difference[num - k] += 1
            difference[num + k + 1] -= 1

        max_frequency = 0
        cumulative_sum = 0

        for value, delta in sorted(difference.items()):

            cumulative_sum += delta

            max_frequency = max(
                max_frequency,
                min(cumulative_sum, frequency[value]+numOperations)
            )


        return max_frequency