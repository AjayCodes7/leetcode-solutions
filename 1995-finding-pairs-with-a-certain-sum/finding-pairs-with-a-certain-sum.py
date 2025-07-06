class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.numbers1 = nums1
        self.numbers2 = nums2
        self.freq1 = Counter(self.numbers1)
        self.freq2 = Counter(self.numbers2)

    def add(self, index: int, val: int) -> None:
        self.freq2[self.numbers2[index]] -= 1
        self.numbers2[index] += val
        self.freq2[self.numbers2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num, freq in self.freq1.items():
            if num >= tot:
                continue
            if tot - num in self.freq2:
                count += self.freq2[tot - num] * freq
        return count



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)