import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for from_city, to_city, price in flights:
            if from_city not in graph:
                graph[from_city] = []
            graph[from_city].append((to_city, price))

        pq = [(0, src, 0)]
        min_cost = {}

        while pq:
            cost, city, stops = heapq.heappop(pq)
            if city == dst:
                return cost

            if stops > k:
                continue

            if city in min_cost and stops >= min_cost[city]:
                continue

            min_cost[city] = stops

            if city in graph:
                for neighbor, neighbor_cost in graph[city]:
                    heapq.heappush(pq, (cost + neighbor_cost, neighbor, stops + 1))

        return -1

def tests(n: int, flights: [[int]], src: int, dst: int, k: int):
    solution = Solution()
    return solution.findCheapestPrice(n, flights, src, dst, k)

result = tests(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
print(result)
