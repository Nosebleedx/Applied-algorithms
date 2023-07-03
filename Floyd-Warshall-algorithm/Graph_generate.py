import random
import csv
import configparser




config = configparser.ConfigParser()
config.read("cfg.ini")

N = int(config["Jija"]["vershini"])
max_connections = int(config["Jija"]["max_connections"])
file = config["Jija"]["filename"]
weight = int(config["Jija"]["weight"])
def create():
    def printf2(file, massiv):
        dictlist = []
        outfile = open('{}.csv'.format(file), 'w', newline='')
        writer = csv.writer(outfile, delimiter=';', quotechar='"')
        for i in range(len(massiv)):
            for key, value in massiv[i].items():
                dictlist.append(key)
                dictlist.append(value)
            j = 0
            writer.writerow(dictlist)
            j += 1
            dictlist.clear()
        outfile.close()

    def generate():
        A = []
        B = list(range(N))
        massiv = []
        for i in range(N):
            massiv.append({})
        c = random.choice(B)
        B.remove(c)
        A.append(c)
        while B:
            c = random.choice(B)
            d = random.choice(A)
            massiv[c][d] = random.randint(1, weight)
            B.remove(c)
            A.append(c)
        for i in range(N):
            if len(massiv[i]) != 0:
                rand = random.randint(1, (max_connections - 1))
            else:
                rand = random.randint(1, max_connections)
            for j in range(rand):
                massiv[i][random.randint(1, N - 1)] = random.randint(1, weight)
        printf2(file, massiv)



    generate()
create()
