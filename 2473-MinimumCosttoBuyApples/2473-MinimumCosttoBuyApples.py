            heap = [(0, start_city)]
            min_cost = float("inf")

            while heap:
                travel_cost, current_city = heapq.heappop(heap)
                min_cost = min(min_cost, appleCost[current_city]+ (k+1)*travel_cost)

            travel_costs[start_city] = 0
            travel_costs = [float("inf") for _ in range(n)]
        def shortest_path(start_city, graph):

            graph[city_b - 1].append((city_a-1, cost))
            graph[city_a - 1].append((city_b-1, cost))
        for city_a, city_b, cost in roads:

        graph = [[] for _ in range(n)]
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
class Solution:
4
