import random
import time
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
num_vertices_left = int(config['Graph']['left_'])
num_vertices_right = int(config['Graph']['right_'])
max_weight = int(config['Graph']['max_w'])

def generate_graph(num_vertices_left, num_vertices_right, max_weight):
    graph = {}
    for i in range(num_vertices_left):
        graph[i] = {}
        for j in range(num_vertices_left, num_vertices_left + num_vertices_right):
            graph[i][j] = random.randint(1, max_weight)
            graph[j] = {}
    return graph

def output_graph(graph, filename):
    with open(filename, "w") as file:
        for i in graph:
            for j in graph[i]:
                file.write(f"{i} {j} {graph[i][j]}\n")


def change_graph_to_matrix(graph, num_vertices_left, num_vertices_right):
    matrix = []
    for i in range(num_vertices_left):
        row = []
        for j in range(num_vertices_left, num_vertices_left + num_vertices_right):
            row.append(graph[i][j])
        matrix.append(row)
    return matrix

def output_matrix(matrix, filename):
    with open(filename, "w") as file:
        for row in matrix:
            file.write(" ".join(str(x) for x in row) + "\n")

start = time.time()


graph = generate_graph(num_vertices_left, num_vertices_right, max_weight)
output_graph(graph, "bipartite graph.txt")

matrix = change_graph_to_matrix(graph, num_vertices_left, num_vertices_right)
output_matrix(matrix, "output_matrix.txt")

print(time.time()-start)