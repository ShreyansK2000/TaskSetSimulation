import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

'''
Setting up points to plot a simplex for visualization
'''
def getSimplexPoints():
    # Plane equation coordinates.
    # For 3 simplex: x + y + z = 1
    a,b,c,d = 1,1,1,1

    x = np.linspace(0,1,200)
    y = np.linspace(0,1,200)

    SimplexX,SimplexY = np.meshgrid(x,y)
    SimplexZ = (d - a*SimplexX - b*SimplexY) / c
    SimplexZ[SimplexZ < 0.] = np.NaN

    return SimplexX, SimplexY, SimplexZ



def plotSimplex(ax):
    SimplexX, SimplexY, SimplexZ = getSimplexPoints()

    # Create cubic bounding box to simulate equal aspect ratio
    max_range = np.array([SimplexX.max()-SimplexX.min(), SimplexY.max()-SimplexY.min(), SimplexZ.max()-SimplexZ.min()]).max()
    Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(SimplexX.max()+SimplexX.min())
    Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(SimplexY.max()+SimplexY.min())
    Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(SimplexZ.max()+SimplexZ.min())

    # for xb, yb, zb in zip(Xb, Yb, Zb):
    #     ax.plot([xb], [yb], [zb], 'w')

    # Make a 3D quiver plot
    x, y, z = np.zeros((3,3))
    u, v, w = np.array([[1,0,0],[0,1,0],[0,0,1]])
    ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1, color="black")
    ax.grid(False)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_zlim(0,1)

    # ax.azim = 20
    surf = ax.plot_surface(SimplexX, SimplexY, SimplexZ, rcount=200, ccount=200, alpha=0.1, shade=False)
    # ax.hold(True)

    return ax

if __name__ == '__main__':
    fig = plt.figure()
    # Add an axes
    ax = fig.add_subplot(111,projection='3d')
    ax = plotSimplex(ax)


    plt.show()
