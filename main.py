from tensor import Tensor
import copy
import matplotlib.pyplot as plt
from visuals import ZeroDim,OneDim,TwoDim
import numpy as np
import random
import time

welcome = "Hello the aventurer! Welcome to the Linear Space. What's your name?"
instruction = """Welcome {}.Where you at now is the linear space of dimension 0 (scalar).\n
Your job is finding friends and using your skills with them to upgrade your level and learn new skills.\n
The way that exp is calculated is based on your dimension of space.\n
At scalar (dimension 0), exp = absolute value of the number.\n
At vector (dimension 1), exp = length of the vector.\n
At matrix (dimension 2), exp = determinant of the matrix.\n"""
scalar_action = """Please choose your action with your buddies. You have the following choices.\n
Multiplication : enter 0.\n
Addition: enter 1.\n"""
choose_action = """Please choose the friend that you want to interact with!\n
"""
vector_action = """Please choose your action with your buddies. You have the following choices.\n
Vector dot product : enter 0.\n
Vector cross product: enter 1.\n
Vector element-wise addition : enter 2.\n
Vector element-wise multiplication : enter 3.\n"""
vector_action_explain = """If you choose the vector cross or dot product. The exp will be updated based on the
value of the result of the product.\n
The dot product of two vectors a = [a1, a2, …, an] and b = [b1, b2, …, bn] is defined as:\n
a.b = a1*b1 + a2*b2 +....+an*bn.\n
The cross product of two vectors a and b is defined as:\n
axb = |a|*|b|*sin(theta) where theta is the angle btwn 2 vectors.\n"""
matrix_action = """Please choose your action with your buddies. You have the following choices.\n
Multiplication : enter 0.\n
Addition: enter 1.\n"""
def create_buds(dimension):
    colors = ['green','blue','magenta']
    if dimension == 0:
        bud1 = Tensor(1, random.randint(1,5), 'green')
        bud2 = Tensor(1, random.randint(1,5), 'blue')
        bud3 = Tensor(1, random.randint(1,5), 'magenta')
        return [bud1,bud2,bud3]
    elif dimension == 1:
        bud1 = Tensor(1, np.random.randint(5, size=2), 'green')
        bud2 = Tensor(1, np.random.randint(5, size=2), 'blue')
        bud3 = Tensor(1, np.random.randint(5, size=2), 'magenta')
        return [bud1,bud2,bud3]
    elif dimension == 2:
        bud1 = Tensor(1, np.random.randint(5, size=(2,2)), 'green')
        bud2 = Tensor(1, np.random.randint(5, size=(2,2)), 'blue')
        bud3 = Tensor(1, np.random.randint(5, size=(2,2)), 'magenta')
        return [bud1,bud2,bud3]
def main():
    name = input(welcome)
    time.sleep(0.5)
    print(instruction.format(name))
    time.sleep(2)
    me = Tensor(0,random.randint(1,5),'red')
    print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.values))
    buds = create_buds(me.dimension)
    while me.values < 100:
        buds = create_buds(me.dimension)
        print("Please meet your new buddies. \nBud 1 (green) : {} exp, Bud 2 (blue) : {} exp, Bud 3 (pink): {} exp.\n".format(buds[0].values,
                                                                                                   buds[1].values,
                                                                                                   buds[2].values))
        action = eval(input(scalar_action))
        while not action in [0,1]:
            action = eval(input(scalar_action))
        chosen = eval(input(choose_action))
        while not chosen in [1,2,3]:
            chosen = eval(input(choose_action))
        if action == 0:
            me.values *= buds[chosen - 1].values
        else:
            me.values += buds[chosen - 1].values
        me.update_exp()    
        print("Here is the visualization of you and your buddies. Your color is red.\n")
        one_D = ZeroDim(me, buds)
        print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.exp))
        time.sleep(2)
    else:
        print("Congratulation! You have moved to the next dimension - vector space.\n")
    me = Tensor(1,[1, 1],'red')
    print("Now you will be a vector {}".format(me.values))
    print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.exp))
    buds = create_buds(me.dimension)
    print(vector_action_explain)
    while me.exp < 100:
        buds = create_buds(me.dimension)
        print("Please meet your new buddies. \nBud 1 (green) : {} exp, Bud 2 (blue) : {} exp, Bud 3 (pink): {} exp.\n".format(buds[0].values,
                                                                                                   buds[1].values,
                                                                                                   buds[2].values))
        action = eval(input(vector_action))
        while not action in [0,1,2,3]:
            action = eval(input(vector_action))
        chosen = eval(input(choose_action))
        while not chosen in [1,2,3]:
            chosen = eval(input(choose_action))
        if action == 0:
            me._dot_product(buds[chosen - 1])
        elif action == 1:
            me._cross_product(buds[chosen - 1])
        elif action == 2:
            me._element_wise_add(buds[chosen - 1])
        else:
            me._elemen_wise_multiply(buds[chosen - 1])
        print("Here is the visualization of you and your buddies. Your color is red.\n")
        one_D = OneDim(me, buds)
        print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.exp))
        time.sleep(2)
    else:
        print("Congratulation! You have moved to the next dimension - matrix space.\n")
    me = Tensor(2,np.random.randint(5, size=(2,2)),'red')
    print("Now you will be a matrix of {}".format(me.values))
    print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.values))
    buds = create_buds(me.dimension)
    while me.values < 100:
        buds = create_buds(me.dimension)
        print("Please meet your new buddies. \nBud 1 (green) : {} exp, Bud 2 (blue) : {} exp, Bud 3 (pink): {} exp.\n".format(buds[0].values,buds[1].values,buds[2].values))                                                                                               
        action = eval(input(scalar_action))
        while not action in [0,1]:
            action = eval(input(scalar_action))
        chosen = eval(input(choose_action))
        while not chosen in [1,2,3]:
            chosen = eval(input(choose_action))
        if action == 0:
            me.values *= buds[chosen - 1].values
        else:
            me.values += buds[chosen - 1].values
        me.update_exp()    
        print("Here is the visualization of you and your buddies. Your color is red.\n")
        print("Your exp now is {}. Try to get over 100 then you will move to the next level.\n".format(me.exp))
        time.sleep(2)
    else:
        print("Congratulation! You win.\n")
if __name__ == "__main__":
    main()