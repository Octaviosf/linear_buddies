# visualizations for linear_buddies

import matplotlib.pyplot as plt
import numpy as np
from tensor import Tensor

class OneDim:
    def __init__(self, me, buds):
        # set figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.xlim(-8, 8)
        plt.ylim(-8, 8)
        plt.grid(True)

        origin = [0], [0]
        bud1 = buds[0]
        bud2 = buds[1]
        bud3 = buds[2]

        V = np.array([me.values, bud1.values, bud2.values, bud3.values])

        colors = [me.color, bud1.color, bud2.color, bud3.color]
        print(V)

        plt.quiver(*origin, V[:, 0], V[:, 1], color=colors, angles='xy', scale_units='xy', scale=1)
        plt.show()



def main():

    me = Tensor(1, [2, 2], 'red')
    bud1 = Tensor(1, [3, -5], 'green')
    bud2 = Tensor(1, [1, 3], 'blue')
    bud3 = Tensor(1, [-1, -4], 'magenta')
    buds = [bud1, bud2, bud3]

    one_D = OneDim(me, buds)

main()



