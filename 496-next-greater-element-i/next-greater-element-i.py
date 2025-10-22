class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = dict()
        stack = []
        for i in nums2[::-1]:
            if stack:
                if stack[-1] > i:
                    nextGreater[i] = stack[-1]
                else:
                    while stack and stack[-1] < i:
                        stack.pop()
                    if stack:
                        nextGreater[i] = stack[-1]
                    else:
                        nextGreater[i] = -1
            else:
                nextGreater[i] = -1
            stack.append(i)
        for i in range(len(nums1)):
            nums1[i] = nextGreater[nums1[i]]
        return nums1
