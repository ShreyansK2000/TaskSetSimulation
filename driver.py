from plot3d import *
from random_vector_generator import *
import matplotlib.pyplot as plt

def main():

    n = 3
    num_points = 2000
    scatter_arr = np.zeros(shape=(num_points, n))

    for i in range(num_points):
        scatter_arr[i] = getUniformVector(getNRandom(n))


    fig = plt.figure(figsize=(8, 8))
    # Add an axes
    ax = fig.add_subplot(111,projection='3d')
    # ax.set_proj_type('ortho')
    ax.view_init(30, 45) 
    ax = plotSimplex(ax)
    # ax.set_aspect(1 / ax.get_data_ratio())
    ax.scatter(scatter_arr[:,0], scatter_arr[:,1], scatter_arr[:,2], marker="o", s=2, depthshade=False)


    plt.show()

if __name__ == '__main__':
    main()