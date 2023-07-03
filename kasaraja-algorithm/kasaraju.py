import csv
import sys
import time

sys.setrecursionlimit(10 ** 6)

def kosaraju(graph):
    visited = [False] * len(graph)
    stack = []

    def dfs1(n):
        visited[n] = True
        for sosed in graph[n]:
            if not visited[sosed]:
                dfs1(sosed)
        stack.append(n)

    for node in range(len(graph)):
        if not visited[node]:
            dfs1(node)

    visited = [False] * len(graph)

    comps = []

    def dfs2(node, component):
        visited[node] = True
        component.append(node)
        for sosed in graph[node]:
            if not visited[sosed]:
                dfs2(sosed, component)

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            comps.append(component)

    return comps

graph = []

Start_time = time.time()

with open('oriented_graph.csv', 'r') as file:
    reader = csv.reader(file)
    for stroka in reader:
        graph.append(list(map(int, stroka)))

components = kosaraju(graph)

with open('outputtt.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for stroka in components:
        writer.writerow(stroka)

print(f'Время выполнения программы:{time.time() - Start_time} секунд')