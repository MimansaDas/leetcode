from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    res = dfs(nei, dst, visited)
                    if res != -1.0:
                        return weight * res

            return -1.0

        ans = []

        for src, dst in queries:
            ans.append(dfs(src, dst, set()))

        return ans