import csv
import configparser
import time
from collections import deque


startTime = time.time()
config = configparser.ConfigParser()
config.read('config.ini')

filename = "graph.csv"


with open('graph.csv') as f:
    reader = csv.reader(f)
    graph = []
    for row in reader:
        for i in row:
            if i:
                graph.append(list(i.split(';')))

for row in graph:
    for i in range(len(row)):
        try:
            row[i] = int(row[i])
        except ValueError:
            row[i] = 0

result = []
for j in range(len(graph)):
    for i in range(0, len(graph[j])-1, 2):
        if i+1 < len(graph[j]):
            node2 = graph[j][i]
            weight = graph[j][i+1]
            result.append((j+1, node2, weight))

def bfs(graph, s, t):
    queue = deque([s])
    dist = {s: 0}
    blocking_flow = {s: float('inf')}
    path = {s: []}
    while queue:
        u = queue.popleft()
        for v, capacity in graph[u].items():
            if v not in dist and capacity > 0:
                dist[v] = dist[u] + 1
                blocking_flow[v] = min(blocking_flow[u], capacity)
                path[v] = path[u] + [(u, v)]
                queue.append(v)

    if t not in dist:
        return None, None
    else:
        return path[t], blocking_flow[t]


def dinic(graph, s, t):
    flow = 0
    ways = []
    while True:
        way, blocking_flow = bfs(graph, s, t)
        if way is None:
            break
        flow += blocking_flow
        u = t
        while u != s:
            for edge in way:
                graph[edge[0]][edge[1]] -= blocking_flow
                graph[edge[1]][edge[0]] += blocking_flow
            u = way[0][0]
        ways.append((way, blocking_flow))
        print("Путь: ", way, 'Поток =', blocking_flow)

    return flow

graph = {}
for u, v, capacity in result:
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = capacity
    graph[v][u] = 0
s = 1
t = max(graph.keys()) - 1
max_flow = dinic(graph, s, t)

print("Макс флоу ", max_flow)
print(f"Сделано за {time.time() - startTime} секунд.")
