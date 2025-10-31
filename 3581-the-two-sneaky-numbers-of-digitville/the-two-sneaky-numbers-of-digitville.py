class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # count = [0]*len(nums)
        # result = []
        # for n in nums:
        #     count[n] += 1
        #     if count[n] == 2:
        #         result.append(n)
        # return result

        visited = set()
        result = []
        for n in nums:
            if n in visited:
                result.append(n)
            else:
                visited.add(n)
        return result