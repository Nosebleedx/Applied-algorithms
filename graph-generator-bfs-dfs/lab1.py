import random
import csv
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
N = int(config["Graph"]["N"])
v_cnt = int(config["Graph"]['vershini'])
file = config["Graph"]['file']

def savefile(file,massiv):
    outfile = open('{}.csv'.format(file), 'w', newline='')
    writer = csv.writer(outfile, delimiter=',', quotechar='"')
    i = 0
    for line in massiv:
        writer.writerow(line)
        i += 1
    outfile.close()

def notoriented_gengraph(N,v_cnt,file):
    a = []
    b = list(range(N))
    graph = []
    for i in range(N):
        graph.append([])
    c = random.choice(b)
    b.remove(c)
    a.append(c)
    while (b != []):
        c = random.choice(b)
        #d = random.choice(a)
        #graph[c].append(d)
        #graph[d].append(c)
        b.remove(c)
        a.append(c)
    for i in range(N):
        rand = random.randint(1, v_cnt)
        count = 0
        lenght = rand - len(graph[i])
        if lenght > 0:
            while count != lenght and len(graph[i]) < v_cnt:
                var = random.randint(0, N - 1)
                if len(graph[var]) < v_cnt and var != i and graph[var] != i:
                    graph[i].append(var)
                    graph[var].append(i)
                    count += 1
    result = []
    for elem in graph:
        graph_elem = list(set(elem))
        result.append(graph_elem)
    print(result)
    links = [len(
        [ i for i in result if len(i)==k]
    )for k in range(101)]

    print(links)
    print(sum(links))
    savefile(file, result)

notoriented_gengraph(N, v_cnt, file)
