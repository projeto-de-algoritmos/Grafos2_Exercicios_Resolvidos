import heapq

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: [[int]]) -> [[int]]:
        def prim(edges, extra_edge=None):
            visited = [False] * n
            edge_list = [[] for _ in range(n)]
            for i, (u, v, w) in enumerate(edges):
                edge_list[u].append((v, w, i))
                edge_list[v].append((u, w, i))

            weight = 0
            pq = []

            # Adiciona uma aresta na AGM
            if extra_edge is not None:
                u, v, w = edges[extra_edge]
                visited[u] = True
                visited[v] = True
                weight += w
                for nxt, w, idx in edge_list[u]:
                    heapq.heappush(pq, (w, nxt, idx))
                for nxt, w, idx in edge_list[v]:
                    heapq.heappush(pq, (w, nxt, idx))
            else:
                heapq.heappush(pq, (0, 0, -1))

            while pq:
                w, v, idx = heapq.heappop(pq)
                if not visited[v]:
                    visited[v] = True
                    weight += w
                    for nxt, nxt_w, nxt_idx in edge_list[v]:
                        if not visited[nxt]:
                            heapq.heappush(pq, (nxt_w, nxt, nxt_idx))

            if sum(visited) != n:  # Grafo não é conectado
                return float('inf')

            return weight

        # Encontra o peso total da arvore geradora minima
        mst_weight = prim(edges)

        criticals, pseudo_criticals = [], []

        # Remove uma aresta por vez do grafo e calcula o peso da AGM sem essa aresta,
        # se o peso for maior que o da AGM original a aresta removida é critica.
        for i in range(len(edges)):
            new_weight = prim(edges[:i] + edges[i+1:])
            if new_weight > mst_weight:
                criticals.append(i)

        # Adiciona uma aresta por vez, que não é crítica, na arvore geradora minima,
        # se o peso da AGM continuar o mesmo a aresta adicionada é pseudo-critica.
        for i in range(len(edges)):
            if i not in criticals:
                new_weight = prim(edges, i)
                if new_weight == mst_weight:
                    pseudo_criticals.append(i)

        return [criticals, pseudo_criticals]


def tests(n: int, edges: [[int]]):
    solution = Solution()
    return solution.findCriticalAndPseudoCriticalEdges(n, edges)

result = tests(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])
print(result)