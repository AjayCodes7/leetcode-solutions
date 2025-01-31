class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = defaultdict(list)
        for pre, crs in prerequisites:
            prereq[crs].append(pre)
        

        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()
                for pre in prereq[crs]:
                    prereqmap[crs] |= dfs(pre) 
                prereqmap[crs].add(crs)
            return prereqmap[crs]
        
        prereqmap = {}
        for crs in range(numCourses):
            dfs(crs)


        result = []
        for u, v in queries:
            result.append(u in prereqmap[v])
        return result