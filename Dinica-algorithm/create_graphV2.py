import csv
import random
import configparser


config = configparser.ConfigParser()
config.read("config.ini")

N = int(config["Graph"]["N"])
v_cnt = int(config["Graph"]['v_cnt'])
max_w = int(config["Graph"]['max_w'])


def write_graph(graph):
    dictlist = []
    outfile = open('graph.csv', 'w', newline='')
    writer = csv.writer(outfile, delimiter=';', quotechar='"')
    for i in range(len(graph)):
        for key, weight in graph[i].items():
            dictlist.append(key)
            dictlist.append(weight)
        j = 0
        writer.writerow(dictlist)
        j += 1
        dictlist.clear()
    outfile.close()


def generate_orient(t, max, w):
    A = []
    B = list(range(t))
    massiv = []
    for i in range(t):
        massiv.append({})
    c = random.choice(B)
    B.remove(c)
    A.append(c)
    while (B != []):
        c = random.choice(B)
        d = random.choice(A)
        massiv[c][d] = random.randint(1, w)
        B.remove(c)
        A.append(c)
    for i in range(t):
        if len(massiv[i]) != 0:
            rand = random.randint(1, (max - 1))
        else:
            rand = random.randint(1, max)
        for j in range(rand):
            massiv[i][random.randint(1, t - 1)] = random.randint(1, w)
    write_graph(massiv)


generate_orient(N, v_cnt, max_w)