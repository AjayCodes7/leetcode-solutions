class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        powers = []
        for i, val in enumerate(bin(n)[2:][::-1]):
            if val == '1':
                powers.append(2**i)
        answer = []
        for query in queries:
            temp = powers[query[0]]
            for i in range(query[0]+1,query[1]+1):
                temp *= powers[i]
            answer.append(temp%mod)
        return answer