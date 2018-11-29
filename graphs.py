#!/usr/bin/env python3
import csv, numpy as np

# -------------------------------- parameters -------------------------------- #
filename = "csv/Figure9_IT.csv"
output_file = "output.csv"
v = 15
r = 1
c = r * v
l = 500

nb_var = 2
var_select = 2

# ------------------------------ preprocessing ------------------------------- #
# On se débarasse de parties pas utiles du fichier

file_str = open(filename).read().split('\n\n')[-1]

open("csv/temp.csv", "w").write('\n'.join(file_str.split('\n')[1:]))

# ------------------------------- csv reading -------------------------------- #

columns = [[] for i in range(c)]
with open("csv/temp.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        row = row[1:]
        assert c * nb_var == len(row), "met les bon paramètres, banane." # nombre de colonnes
        for i in range(c):
            columns[i].append(float(row[i * nb_var + var_select - 1]))
# [ 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 | 0 0 0 ]
#     _       _       _       _       _       _       _
#     1       4       7
data = np.array(columns)

# ───────────────────────── c'est ton moment, Maxime ───────────────────────── #

results = [[ 0 for i in range(r + 1)] for i in range(l + 1)] # Ligne 1 : ticks [1 - l]
for i, row in enumerate(results):
    row[0] = i
    for j in range(r):
        row[j + 1] = np.mean(data[j * v:(j + 1) * v, i])

# print(data)
# print(np.array(results)[1])

# print(data[:,1])

with open(output_file, 'w') as out:
    writer = csv.writer(out, delimiter=';')
    for row in results:
        writer.writerow(['{:.7}'.format(','.join(str(elt).split('.'))) for elt in row])
