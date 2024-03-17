from math import inf
import heapq
import sys

input = sys.stdin.readline

def dijkstra(v):
    heap = [(0, v)]
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

n, m = [int(input()) for _ in range(2)]
adj = [[] for _ in range(n + 1)]
distance = [inf for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    adj[v1].append((v2, w))

v, destination = map(int, input().split())

dijkstra(v)

print(distance[destination])