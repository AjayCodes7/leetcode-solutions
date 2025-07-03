class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'
        gs = []
        word = [97]
        while len(word) < k:
            if not len(gs):
                gs.append(98)
            else:
                initial_length = len(gs)
                l = 0
                while l < initial_length*2:
                    gs.insert(l+1, gs[l]+1 if gs[l]+1 < 123 else 98)
                    l += 2
            word.extend(gs)
        return chr(word[k-1])