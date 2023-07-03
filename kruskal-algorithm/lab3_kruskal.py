import random
import csv
import configparser
import time

config = configparser.ConfigParser()
config.read("config.ini")
N = int(config['Graph']['vershini'])
max_v = int(config['Graph']['max_v'])


class Graph:
    def __init__(self, n, connections):
        self.n = n
        self.connections = connections
        self.graph = [[] for _ in range(n)]

    def generate_graph(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if len(self.graph[i]) < self.connections and len(self.graph[j]) < self.connections:
                    weight = random.randint(1, 15)
                    self.graph[i].append((j, weight))
                    self.graph[j].append((i, weight))
        self._write_csv()
        return self.graph

    def _write_csv(self):
        with open("vhodnoi_graph.csv", "w", newline='') as file:
            write = csv.writer(file)
            for i in range(self.n):
                stroka = [str(i)]
                for j, weight in self.graph[i]:
                    stroka.append(str(j) + ',' + str(weight))
                write.writerow(stroka)

    def poisk_uzla(self, parent, i):
        if parent[i] == i:
            return i
        return self.poisk_uzla(parent, parent[i])

    def soedinenie(self, parent, s, x, y):
        xroot = self.poisk_uzla(parent, x)
        yroot = self.poisk_uzla(parent, y)
        if xroot == yroot:
            return
        if s[xroot] < s[yroot]:
            xroot, yroot = yroot, xroot
        parent[yroot] = xroot
        s[xroot] += s[yroot]

    def algorithm(self):
        vert = len(self.graph)
        edges = []
        for i in range(vert):
            for j, weight in self.graph[i]:
                edges.append((weight, i, j))
        edges.sort()
        parents = [i for i in range(vert)]
        si = [1] * vert
        result = [[] for _ in range(vert)]
        for weight, u, v in edges:
            if self.poisk_uzla(parents, u) != self.poisk_uzla(parents, v):
                self.soedinenie(parents, si, u, v)
                result[u].append((v, weight))
                result[v].append((u, weight))
        return result


Start_Time = time.time()

kruslall = Graph(N, max_v)
graph = kruslall.generate_graph()
#print(graph)
derevo_kruskalla = kruslall.algorithm()


with open("output_graph.csv", "w", newline='') as file:
    write = csv.writer(file)
    for i in range(len(derevo_kruskalla)):
        stroka = [str(i)]
        for j, weight in derevo_kruskalla[i]:
            stroka.append(str(j) + "," + str(weight))
        write.writerow(stroka)


print(f'Время выполнения программы: {time.time() - Start_Time} секунд.')