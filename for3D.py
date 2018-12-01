#!/usr/bin/env python3
import csv, numpy as np, matplotlib, matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter, AutoLocator
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------- parameters -------------------------------- #
filename = "csv/pour3DGrand.csv"
output_file = "output.csv"
nb_iter = 8
span1 = 5 # number of values of var 1
span2 = 5 # ------------------- var 2
defspace1 = [1, 5]
defspace2 = [1, 5]
total_span = span1 * span2
ticks = 150

# ------------------------------ preprocessing ------------------------------- #
# On se débarasse de parties pas utiles du fichier
def preprocess(filename):
    """
    Preprocesses a file and writes the result in a temporary file.
    Returns a file object of that temporary file.
    """
    file_str = open(filename).read().split('\n\n')[-1]
    open("csv/temp.csv", "w").write('\n'.join(file_str.split('\n')[1:]))
    return open("csv/temp.csv")

# ------------------------------- csv reading -------------------------------- #
def extract_data_3d(file_object):
    data = np.zeros((span1, span2)) # span1 * span2 * 1
    with file_object as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(reader):
            if i == ticks: # On garde que le dernier
                row = row[1:] # On enlève les ticks
                assert total_span * nb_iter == len(row), "met les bon paramètres, banane." # nombre de colonnes
                for s1 in range(span1): # for W_C
                    for s2 in range(span2): # for W_W
                        s = s1 * span1 + s2
                        # columns[i].append(float(row[i * nb_var + var_select - 1]))
                        s_iters = row[s * nb_iter: (s + 1) * nb_iter] # on prend les nb_iter iterations
                        data[s1,s2] = np.mean([float(x) for x in s_iters])
    return data

# --------------------- discretize the definition space ---------------------- #
def discretise_space(def_space, n = 100):
    """
    Discretise an n-dimensional space with equally spaced points.
        see np.meshgrid
    """
    dim = len(def_space)
    one_dim_axis = [] # list of coordinates on 1 dim axis
                      # ex : [ x, y ]
                      # x = [0, 0.1, .., 0.9, 1]
                      # y = [2, 2.1, .., 2.9, 3]
    for i in range(dim):
        start, stop = def_space[i]
        one_dim_axis.append(np.linspace(start, stop, n))
    return np.meshgrid(*one_dim_axis)



# -------------- plot a 2 dimensional function in a 3D diagram --------------- #
def plot3d(data):
    """ Plots a two dimensional function on a 3 dimensional graph """
    assert span1 == span2
    span = span1
    # ---------------------- create the figure and axes ---------------------- #
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # -- discretize the definition space and compute the function's images --- #
    X, Y = discretise_space([defspace1, defspace2], n=span)
    Z = data

    # ----------------------- appearance and plotting ------------------------ #
    ax.set_zlim(np.min(Z) - 0.5, np.max(Z) + 0.5)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set(xlabel='$W\_C$', ylabel='$W\_W$', zlabel="Utilité")#,
            # title='Utilité à {} ticks en fonction de W_W et W_C'.format(ticks))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, alpha=0.8, #, cmap='binary'
               linewidth=0, antialiased=False, zorder=1)

    plt.show()

# ---------------------- plot with levels instead of 3D ---------------------- #
def plotLevels(data):
    assert span1 == span2
    span = span1
    # ---------------------- create the figure and axes ---------------------- #
    fig, ax = plt.subplots()

    # -- discretize the definition space and compute the function's images --- #
    X, Y = discretise_space([defspace1, defspace2], n=span)
    Z = data

    cs = ax.contourf(X, Y, Z, locator=AutoLocator(), cmap=cm.PuBu)

    # ---------------------------- titles & misc ----------------------------- #
    cbar = fig.colorbar(cs) # bar with scales

    ax.set(xlabel='$W\_C$', ylabel='$W\_W$')#,
            #title='Utilité à {} ticks en fonction de W_W et W_C'.format(ticks))
    plt.show()

if __name__ == '__main__':
    data = extract_data_3d(preprocess(filename))
    plotLevels(data)
    # plot3d(data)

# ──────────────────────────────── Figure 3D ───────────────────────────────── #
