import random
import networkx as nx
import matplotlib.pyplot as plt
import configparser
import csv
import time

config = configparser.ConfigParser()
config.read('cfg.ini')

nodes_count = config.getint('Jija', 'vershini')
max_edges = config.getint('Jija', 'max_connections')
max_capacity = config.getint('Jija', 'weight')
filename = config.get('Jija', 'filename')

def oriented_weight_graph(nodes_count, max_edges, max_capacity):
    nodes = list(range(1, nodes_count + 1))
    result = []
    for i in range(nodes_count):
        max_edges_for_node = min(max_edges, len(nodes) - 1)
        available_nodes = nodes[:i] + nodes[i + 1:]
        edges_count = min(max_edges_for_node, len(available_nodes))
        edges = random.sample(available_nodes, edges_count)
        node_edges = [(v, random.randint(1, max_capacity)) for v in edges]
        result.append(node_edges)
    return result

def flatten_list(lst):
    return [[elem for tpl in inner_lst for elem in tpl] for inner_lst in lst]

def printfile(file, res):
    outfile = open('{}.csv'.format(file), 'w', newline='')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    for line in res:
        writer.writerow(line)
    outfile.close()

startTime = time.time()
graph_edges = oriented_weight_graph(nodes_count, max_edges, max_capacity)
x = flatten_list(graph_edges)
print(graph_edges)
print(x)
print(f"Time - {time.time() - startTime} seconds.")
printfile(filename, x)