import random
import csv
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
N = int(config['Graph']['vershini'])
max_v = int(config['Graph']['max_v'])
fn = 'oriented_graph'
res=[[] * 1 for i in range(N)]

def create_file(filename, graff):
    file = open('{}.csv'.format(filename), 'w', newline='')
    write = csv.writer(file, delimiter = ',', quotechar = '"')
    for line in graff:
        write.writerow(line)
    file.close()

def oriented_graph(n, max_v, filename):
    f = []
    s = list(range(n))
    mass = []
    for i in range(n):
        mass.append(set())
    rand = random.choice(s)
    s.remove(rand)
    f.append(rand)
    while (s != []):
        rand = random.choice(s)
        rand1 = random.choice(f)
        mass[rand].add(rand1)
        s.remove(rand)
        f.append(rand)
    for i in range(n):
        if len(mass[i]) != 0:
            rand = random.randint(1, (max_v - 1))
        else:
            rand = random.randint(1, max_v)
        while len(mass[i]) < rand:
            new_edge = random.randint(0, n - 1)
            if new_edge != i and new_edge not in mass[i]:
                mass[i].add(new_edge)
    mass = [list(x) for x in mass]
    create_file(filename, mass)

oriented_graph(N,max_v,fn)
