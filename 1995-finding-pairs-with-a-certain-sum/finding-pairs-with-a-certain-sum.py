class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.numbers1 = nums1
        self.numbers2 = nums2
        self.freq = Counter(self.numbers2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.numbers2[index]] -= 1
        self.numbers2[index] += val
        self.freq[self.numbers2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for i in self.numbers1:
            if tot - i in self.freq:
                count += self.freq[tot - i]
        return count



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)