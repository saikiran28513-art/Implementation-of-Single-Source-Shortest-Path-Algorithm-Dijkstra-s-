import heapq


def dijkstra(graph, source):
    dist = [float('inf')] * len(graph)
    prev = [None] * len(graph)

    dist[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev


def reconstruct_path(prev, source, target):
    path = []

    while target is not None:
        path.append(target)
        target = prev[target]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# -------- Graph --------
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

source = 0

dist, prev = dijkstra(graph, source)

print("Shortest paths from vertex", source)
print()

print("{:<8} {:<10} {}".format("Vertex", "Distance", "Path"))
print("-" * 45)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    path_str = " -> ".join(map(str, path))
    distance = dist[v] if dist[v] != float('inf') else "INF"

    print("{:<8} {:<10} {}".format(v, distance, path_str))