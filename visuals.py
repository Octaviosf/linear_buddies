# visualizations for linear_buddies

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from tensor import Tensor
import copy


class OneDim:
    def __init__(self, me, buds):
        # find max values for axes
        tensors = copy.deepcopy(buds)
        tensors.insert(0, me)

        max_ = 10
        for t in tensors:
            temp_max = max(abs(t.values))
            if temp_max > 10:
                max_ = temp_max + 0.2 * temp_max

        # set number line
        plt.figure(figsize=(8, 6))
        n = 8

        ax = plt.subplot(n, 1, 6)
        setup(ax)
        ax.xaxis.set_major_locator(ticker.AutoLocator())
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

        plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=1.05)

        plt.xlim(-max_, max_)
        #plt.ylim(-max_, max_)
        plt.grid(True)

        origin = [0], [0]
        bud1 = buds[0]
        bud2 = buds[1]
        bud3 = buds[2]

        V = np.array([me.values, bud1.values, bud2.values, bud3.values])

        colors = [me.color, bud1.color, bud2.color, bud3.color]

        #plt.scatter(V[:, 0], V[:, 1], color=colors)
        plt.quiver(*origin, V[:, 0], V[:, 1], color=colors, angles='xy', scale_units='xy', scale=1)

        plt.show()


def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)


class OneDim2:
    def __init__(self, me, buds):
        # find max values for axes
        tensors = copy.deepcopy(buds)
        tensors.insert(0, me)

        max_ = 10
        for t in tensors:
            temp_max = max(abs(t.values))
            if temp_max > 10:
                max_ = temp_max + 0.2*temp_max

        # set figure
        fig = plt.figure()
        ax = fig.add_subplot(111)

        plt.xlim(-max_, max_)
        plt.ylim(0, 0)
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



class TwoDim:
    def __init__(self, me, buds):
        # find max values for axes
        tensors = copy.deepcopy(buds)
        tensors.insert(0, me)

        max_ = 10
        for t in tensors:
            temp_max = max(abs(t.values))
            if temp_max > 10:
                max_ = temp_max + 0.2*temp_max

        # set figure
        fig = plt.figure()
        ax = fig.add_subplot(111)

        plt.xlim(-max_, max_)
        plt.ylim(-max_, max_)
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


def main1():

    me = Tensor(1, [2, 0], 'red')
    bud1 = Tensor(1, [-5, 0], 'green')
    bud2 = Tensor(1, [3, 0], 'blue')
    bud3 = Tensor(1, [-4, 0], 'magenta')
    buds = [bud1, bud2, bud3]

    me.scalar(4)

    one_D = OneDim(me, buds)


def main2():

    me = Tensor(1, [2, 2], 'red')
    bud1 = Tensor(1, [3, -5], 'green')
    bud2 = Tensor(1, [1, 3], 'blue')
    bud3 = Tensor(1, [-6, -4], 'magenta')
    buds = [bud1, bud2, bud3]

    me.scalar(4)
    me.multiply(bud3)

    one_D = TwoDim(me, buds)


#main2()
main1()

