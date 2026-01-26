class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        minDiff = float('inf')
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < minDiff:
                minDiff = arr[i+1] - arr[i]
                result.clear()
                result.append([arr[i],arr[i+1]])
            elif arr[i+1] - arr[i] == minDiff:
                result.append([arr[i],arr[i+1]])
        return result