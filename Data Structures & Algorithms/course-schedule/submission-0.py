class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pr_map = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses
        q = deque()
        visited = 0

        for a, b in prerequisites:
            pr_map[b].append(a)
            inDegrees[a] += 1
        # print("pr_map: ", pr_map)
        # print("inDegrees: ", inDegrees)

        for idx in range(numCourses):
            if inDegrees[idx] == 0:
                q.append(idx)

        while q:
            cur = q.popleft()
            visited += 1
            for neighbor in pr_map[cur]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)

        # print(visited)
        # print(numCourses)
        return visited == numCourses
