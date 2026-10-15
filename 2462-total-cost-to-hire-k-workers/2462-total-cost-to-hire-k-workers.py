class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1

        heap = []

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[left], left))
                left += 1

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(heap, (costs[right], right))
                right -= 1

        total = 0

        for _ in range(k):
            cost, idx = heapq.heappop(heap)
            total += cost

            if left <= right:
                if idx < left:
                    heapq.heappush(heap, (costs[left], left))
                    left += 1
                else:
                    heapq.heappush(heap, (costs[right], right))
                    right -= 1

        return total

        