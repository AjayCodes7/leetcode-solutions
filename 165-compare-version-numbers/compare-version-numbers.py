class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = 0
        v2 = 0

        pos1 = 0
        pos2 = 0

        n1 = len(version1)
        n2 = len(version2)

        while pos1 < n1 or pos2 < n2:
            v1 = 0
            v2 = 0

            while pos1 < n1 and version1[pos1] != '.':
                v1 = v1 * 10 + int(version1[pos1])
                pos1 += 1
            
            while pos2 < n2 and version2[pos2] != '.':
                v2 = v2 * 10 +  int(version2[pos2])
                pos2 += 1

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1            

            pos1 += 1
            pos2 += 1
    
        return 0