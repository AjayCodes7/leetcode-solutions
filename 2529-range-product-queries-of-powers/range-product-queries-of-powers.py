class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        binStr = bin(n)[2:]
        powers = []
        p = 0
        for i in binStr[::-1]:
            if i == '1':
                powers.append(2**p)
            p += 1
        answer = []
        print(powers)
        for query in queries:
            temp = powers[query[0]]
            for i in range(query[0]+1,query[1]+1):
                temp *= powers[i]
            answer.append(temp%mod)
        return answer