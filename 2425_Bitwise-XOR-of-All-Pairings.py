class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        n1 = 0
        if n % 2 != 0:
            for i in nums1:
                n1 ^= i
        n2 = 0
        if m % 2 != 0:
            for j in nums2:
                n2 ^= j
        return n1^n2