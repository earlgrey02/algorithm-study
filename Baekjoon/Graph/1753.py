from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v):
    heap = []
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

v, e = map(int, input().split())
k = int(input())
adj = [[] for _ in range(v + 1)]
distance = [inf for _ in range(v + 1)]

for _ in range(e):
    v1, v2, w = map(int, input().split())
    adj[v1].append((v2, w))

dijkstra(k)

print(*[distance[i] if distance[i] != inf else "INF" for i in range(1, v + 1)], sep = "\n")