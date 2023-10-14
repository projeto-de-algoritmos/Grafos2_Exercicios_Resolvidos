class Solution:
    def minCostConnectPoints(self, points: [[int]]) -> int:

        # Calcular peso de arestas
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Estrutura union-find
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, i, j):
            iroot = find(parent, i)
            jroot = find(parent, j)
            if rank[iroot] < rank[jroot]:
                parent[iroot] = jroot
            elif rank[iroot] > rank[jroot]:
                parent[jroot] = iroot
            else:
                parent[iroot] = jroot
                rank[jroot] += 1

        n = len(points)
        edges = []

        # Indicar o peso relativo a cada aresta
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((distance, i, j))

        # Ordena as arestas com base no peso
        edges.sort()

        parent = list(range(n))
        rank = [0] * n
        total_cost = 0
        num_edges_added = 0

        # Kruskal
        for edge in edges:
            distance, u, v = edge
            if find(parent, u) != find(parent, v):
                union(parent, rank, u, v)
                total_cost += distance
                num_edges_added += 1
                if num_edges_added == n - 1:
                    break

        return total_cost

def tests(points: [[int]]):
    solution = Solution()
    return solution.minCostConnectPoints(points)

result = tests([[0,0],[2,2],[3,10],[5,2],[7,0]])
print(result)