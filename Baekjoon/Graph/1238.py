from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v, adj):
    heap = []
    distance = [inf for _ in range(n + 1)]
    heapq.heappush(heap, (0, v))
    distance[v] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if distance[v] < w:
            continue

        for next_v, next_w in adj[v]:
            next_w += w

            if next_w < distance[next_v]:
                distance[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))

    return distance

n, m, x = map(int, input().split())
reversedDistance = [inf for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
reversedAdj = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    adj[v1].append((v2, w))
    reversedAdj[v2].append((v1, w))

distance = dijkstra(x, adj)
reversedDistance = dijkstra(x, reversedAdj)

print(max([distance[i] + reversedDistance[i] for i in range(1, n + 1) if i != x]))