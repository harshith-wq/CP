from collections import deque
def ford_fulkerson(V, graph):
    residual = [row[:] for row in graph]
    max_flow = 0
    source = 0
    sink = V - 1
    while True:
        parent = [-1] * V
        parent[source] = source
        queue = deque([source])

        while queue and parent[sink] == -1:
            u = queue.popleft()

            for v in range(V):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)

                    if v == sink:
                        break

        if parent[sink] == -1:
            break
        path_flow = float("inf")
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u
        v = sink

        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow


V, E = map(int, input().split())

graph = [[0] * V for _ in range(V)]

for _ in range(E):
    u, v, capacity = map(int, input().split())
    graph[u][v] += capacity

print(ford_fulkerson(V, graph))
