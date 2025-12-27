class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l = len(customers) + 1
        prefix = [0] * (l)
        postfix = [0] * (l)
        for i in range(1, l):
            if customers[i-1] == 'N':
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
            
            if customers[l-i-1] == 'Y':
                postfix[l-i-1] = postfix[l-i] + 1
            else:
                postfix[l-i-1] = postfix[l-i]
        
        min_penalty, idx = float('inf'), 0
        
        for i in range(l):
            penalty = postfix[i] + prefix[i]

            if penalty < min_penalty:
                min_penalty = penalty
                idx = i

        return idx
