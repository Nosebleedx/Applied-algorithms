import csv
import time

with open('lupa.csv', 'r') as file:
    f = csv.reader(file, delimiter=',')
    cnt = 0
    for i in f:
        cnt += 1


vershini = cnt

def for_dfs():
    graph = {}
    ms = []
    with open('lupa.csv', 'r') as file:
        f = csv.reader(file, delimiter=',')
        for string in f:
            ms.append(string)
        for ind in range(0, vershini):
            massive = []
            for j in range(len(ms[ind])):
                chislo = ms[ind][j]
                massive.append(int(chislo))
            graph[ind] = massive
    return graph

def for_bfs():
    graph = {}
    with open('lupa.csv', 'r') as file:
        f = csv.reader(file, delimiter=',')
        massive = []
        for string in f:
            massive.append(string)
    for ind in range(0, vershini):
        graph[f'{ind}'] = massive[ind]
    return graph

def dfs(graph, begn):
 #   print(graph)
    res = []
    visited = [begn]
    stack = [begn]
    while len(stack) != 0:
        v = stack.pop()
        res.append(v)
        sortt = graph[v]
        #print(sortt)
        sortt = list(filter((lambda sr:sr not in visited), sortt))
        visited.extend(sortt)
        for sr in sortt:
            stack.append(sr)
    return res

def bfs(graph, begn, visited = None):
    otvet = []
    #print(graph)

    res = []
    visited = []
    visited.append(begn)
    res.append(begn)
    while res:
        string = res.pop(0)
        otvet.append(int(string))
        for i in graph[string]:
            if i not in visited:
                visited.append(i)
                res.append(i)
    return otvet

start_prog = time.time()

start_time_dfs = time.time()
print('dfs:')
print(dfs(for_dfs(), 1))
print(f"Время выполнения в глубину {time.time() - start_time_dfs} секунд.")

start_time_bfs = time.time()
print('bfs:')
print(bfs(for_bfs(), '1'))
print(f"Время выполнения в ширину {time.time() - start_time_bfs} секунд.")

print(f"\nПолное время выполнения программы {time.time() - start_prog} секунд.")
