class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False

            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) ==False:
                return []
        return output

        