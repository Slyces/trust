#!/usr/bin/env python3
import csv, numpy as np

# ----------------------- parser pour gagner du temps ------------------------ #
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("--varname", dest="var_name", type=str, default="utility")
parser.add_argument("-v", dest="variation_params", type=int, default=1)
parser.add_argument("-s", dest="select", type=int, default=1)
parser.add_argument("-n", dest="nb_var", type=int, default=1)
parser.add_argument("-i", dest="iterations", type=int, default=10)
parser.add_argument("-t", dest="ticks", type=int, default=250)
args = parser.parse_args()

# -------------------------------- parameters -------------------------------- #
filename = args.file
# output_file = "output.csv"
output_file = args.var_name + '-' + '.'.join(filename.split('.')[:-1]) + '.csv'
iterations = args.iterations
variations_params = args.variation_params
c = variations_params * iterations
ticks = args.ticks

nb_var = args.nb_var
var_select = args.select

# ----------------------- pour windows : décommente ça ----------------------- #
# Et même pas besoin de commenter au dessus

# filename = "file"
# output_file = "output.csv"
# iterations = 10
# variations_params = 1
# c = variations_params * iterations
# ticks = 250
# 
# nb_var = 1
# var_select = 1

# ------------------------------ preprocessing ------------------------------- #
# On se débarasse de parties pas utiles du fichier

file_str = open(filename).read().split('\n\n')[-1]

open("temp.csv", "w").write('\n'.join(file_str.split('\n')[1:]))

# ------------------------------- csv reading -------------------------------- #

columns = [[] for i in range(c)]
with open("temp.csv") as csv_file:
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
    writer = csv.writer(out, delimiter=',')
    for row in results:
        writer.writerow(['{:.7}'.format(','.join(str(elt).split('.'))) for elt in row])
