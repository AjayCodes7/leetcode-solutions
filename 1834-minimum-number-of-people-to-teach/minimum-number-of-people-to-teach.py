class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cntcom = set()
        for friendship in friendships:
            ccom = {}
            conm = False
            for lang in languages[friendship[0]-1]:
                ccom[lang] = 1
            for lang in languages[friendship[1]-1]:
                if lang in ccom:
                    conm = True
                    break
            if not conm:
                cntcom.add(friendship[0]-1)
                cntcom.add(friendship[1]-1)
        
        max_count = 0
        count = [0] * (n+1)
        for friendship in cntcom:
            for lang in languages[friendship]:
                count[lang] += 1
                max_count = max(max_count, count[lang])
        return len(cntcom) - max_count

        