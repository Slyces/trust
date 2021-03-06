#!/usr/bin/env python3
import csv, numpy as np

# -------------------------------- parameters -------------------------------- #
filename = "csv_de_la_nuit/Q2.1.3-1-IT.csv"
output_file = "csv_de_la_nuit/output.csv"
iterations = 10
variations_params = 1
c = variations_params * iterations
ticks = 250

nb_var = 2
var_select = 1

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

results = [[ 0 for i in range(variations_params + 1)] for i in range(ticks + 1)] # Ligne 1 : ticks [1 - ticks]
for i, row in enumerate(results):
    row[0] = i
    for j in range(variations_params):
        row[j + 1] = np.mean(data[j * iterations:(j + 1) * iterations, i])

# print(data)
# print(np.array(results)[1])

# print(data[:,1])

with open(output_file, 'w') as out:
    writer = csv.writer(out, delimiter=';')
    for row in results:
        writer.writerow(['{:.7}'.format(','.join(str(elt).split('.'))) for elt in row])
