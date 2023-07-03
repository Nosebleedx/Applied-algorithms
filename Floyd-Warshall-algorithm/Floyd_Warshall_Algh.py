import time
import numpy as np
from numba import njit, prange
import configparser

config = configparser.ConfigParser()
config.read("cfg.ini")

@njit(parallel=True, nogil=True)
def floyd_warshall(adj_matrix):
    n = adj_matrix.shape[0]
    dist = adj_matrix.copy()
    path = np.zeros((n, n), dtype=np.int64)
    for k in prange(n):
        for i in prange(n):
            for j in prange(n):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    path[i, j] = k

    # Проверка наличия отрицательных путей
    for i in prange(n):
        if dist[i, i] < 0:
            return None, None  # Возвращаем None, если есть отрицательный путь

    return dist, path

def read_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        adj_list = []
        for line in lines:
            values = list(map(int, line.strip().split(';')))
            adj_list.append(values)
    return adj_list

def list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.full((n, n), np.inf, dtype=np.float64)
    for i in range(n):
        for j in range(0, len(adj_list[i]), 2):
            neighbor = adj_list[i][j]
            weight = adj_list[i][j + 1]
            adj_matrix[i, neighbor] = weight
    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix

def write_path_matrix(file_path, path_matrix):
    with open(file_path, 'w') as file:
        n = path_matrix.shape[0]
        for i in range(n):
            for j in range(n):
                file.write(f"{path_matrix[i, j]};")
            file.write("\n")


def floyd_warshall_from_csv(file_path):
    adj_list = read_graph(file_path)
    adj_matrix = list_to_matrix(adj_list)
    dist, path = floyd_warshall(adj_matrix)
    return dist, path

start_time = time.time()
csv_file_path = f'{config["Jija"]["filename"]}.csv'
distances, path = floyd_warshall_from_csv(csv_file_path)

if distances is None:
    print("Граф содержит отрицательные циклы. Кратчайшие пути не могут быть определены.")
else:
    path_matrix_file_path = f'{config["Jija"]["filename"]}_path_matrix.csv'
    distances_matrix_file_path = f'{config["Jija"]["filename"]}_distances_matrix.csv'
    write_path_matrix(distances_matrix_file_path, distances)
    write_path_matrix(path_matrix_file_path, path)
    print(f"Матрица путей записана в {path_matrix_file_path}, за {time.time() - start_time} секунд")
