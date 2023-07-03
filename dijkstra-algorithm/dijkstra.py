import csv
import configparser
import time
import heapq

def dijkstra(G, start, end):
    n = len(G)
    distance = {i+1: float('inf') for i in range(1, n + 1)}  # словарь кратчайших расстояний от начальной вершины
    distance[start] = 0  # расстояние от начальной вершины до самой себя
    visited = set()  # множество посещенных вершин

    while True:
        min_distance = float('inf')
        min_vertex = None
        for v in distance:
            if v not in visited and distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v

        if min_vertex is None:
            break

        visited.add(min_vertex)

        for v, weight in zip(G[min_vertex - 1][::2], G[min_vertex - 1][1::2]):
            if v not in visited and distance[min_vertex] + weight < distance[v]:
                distance[v] = distance[min_vertex] + weight

    if end not in visited:
        return "Граф содержит отрицательный цикл"

    sum = distance[end]
    path = []
    current = end
    while current != start:
        for i in range(n):
            for j in range(1, len(G[i]), 2):
                if G[i][j-1] == current and distance[i+1] + G[i][j] == distance[current]:
                    path.append(current)
                    current = i + 1
                    break
    path.append(start)
    path.reverse()

    return sum, path


def fast_dijkstra(G, start, end):
    n = len(G)
    distance = {i+1: float('inf') for i in range(1, n + 1)}
    distance[start] = 0
    previous = {}

    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if u == end:
            break
        if cost > distance[u]:
            continue
        for v, weight in zip(G[u - 1][::2], G[u - 1][1::2]):
            new_distance = cost + weight
            if new_distance < distance[v]:
                distance[v] = new_distance
                previous[v] = u
                heapq.heappush(heap, (new_distance, v))

    if end not in previous:
        return "Граф содержит отрицательный цикл"

    sum = distance[end]
    path = []
    current = end
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()

    return sum, path


if __name__ == '__main__':
    startTime = time.time()
    config = configparser.ConfigParser()
    config.read('cfg.ini')

    filename = config['Jija']['filename'] + '.csv'

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

    G = graph
    start_vertex = 1
    end_vertex = len(graph)
    result = fast_dijkstra(G, start_vertex, end_vertex)
    print("Кратчайший путь из вершины", start_vertex, "в вершину", end_vertex, ":", result[1])
    print("Суммарный вес кратчайшего пути:", result[0])
    print(f"Completed in {time.time() - startTime} seconds.")
