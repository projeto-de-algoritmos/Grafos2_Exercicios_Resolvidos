# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Dado um grafo ponderado não direcionado e conectado com n vértices numerados de 0 a n - 1, e uma matriz de arestas onde edges[i] = [ai, bi, pesoi] representa uma aresta bidirecional e ponderada entre os nós ai e bi. Uma árvore geradora mínima (AGM) é um subconjunto das arestas do grafo que conecta todos os vértices sem ciclos e com o peso total mínimo possível.

Encontre todas as arestas críticas e pseudo-críticas na árvore geradora mínima (AGM) do grafo dado. Uma aresta da AGM cuja exclusão do grafo aumentaria o peso da AGM é chamada de aresta crítica. Por outro lado, uma aresta pseudo-crítica é aquela que pode aparecer em algumas AGMs, mas não em todas.

Lembrando que você pode retornar os índices das arestas em qualquer ordem.

> Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
>
> Output: [[0,1],[2,3,4,5]]
>
