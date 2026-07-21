import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1

            if not maxHeap:
                break

            w += -heapq.heappop(maxHeap)

        return w