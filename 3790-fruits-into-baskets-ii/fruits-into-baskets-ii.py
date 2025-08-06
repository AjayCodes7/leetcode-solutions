class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        pool = [i for i in range(len(baskets))]
        for fruit in fruits:
            unset = 1
            for i in pool:
                if fruit <= baskets[i]:
                    pool.remove(i)
                    unset = 0
                    break
            count += unset
        return count