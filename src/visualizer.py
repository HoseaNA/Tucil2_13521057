import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi visualisasi pada 3D
def visualize(points, closestPair):
    x = points
    p1 = closestPair[1]
    p2 = closestPair[2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(len(x)):
        ax.scatter(x[i][0], x[i][1], x[i][2], color='b', marker='o')

    ax.scatter(p1[0], p1[1], p1[2], color='r', marker='o')
    ax.scatter(p2[0], p2[1], p2[2], color='r', marker='o')

    ax.set_xlim([-1000, 1000])
    ax.set_ylim([-1000, 1000])
    ax.set_zlim([-1000, 1000])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()
