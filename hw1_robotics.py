# -*- coding: utf-8 -*- 

#################
# Hacettepe University Robotics HW 1
# Written by Selin Cosar
#################

import numpy as np
from sympy import sin, cos, pi


# get Rotation Matrix around X axis by theta degree
def getRx(theta):
    return np.matrix([[1, 0, 0],
                      [0, cos(theta), sin(theta)],
                      [0, sin(theta), cos(theta)]])


# get Rotation Matrix around Y axis by theta degree
def getRy(theta):
    return np.matrix([[cos(theta), 0, -sin(theta)],
                      [0, 1, 0],
                      [-sin(theta), 0, cos(theta)]])


# get Rotation Matrix around Z axis by theta degree
def getRz(theta):
    return np.matrix([[cos(theta), -sin(theta), 0],
                      [sin(theta), cos(theta), 0],
                      [0, 0, 1]])


# 1) Write a function in python (3.x) that will rotate a given 3D point BP = [x,y,z] by angle θ.
# (AP = f1(BP,θ), where f1 is your function) around
def f1(point, angle):
    # a) X-axis
    resultX = np.dot(getRx(angle), point)

    # b) Y-axis
    resultY = np.dot(getRy(angle), point)

    # c) Z-axis
    resultZ = np.dot(getRz(angle), point)

    return resultX, resultY, resultZ


# 2) Test your f1 with BP = [3,5,0] and θ = 90 for all axes.
pB = np.matrix([[3], [5], [0]])
x, y, z = f1(pB, pi / 2)


# print(x)
# print(y)
# print(z)

# 3) Write a function for XYZ fixed angles by using your written func- tions.
# (AP = f2(α,β,γ,B P), where α,β,γ are rotations around X,Y,Z respectively.)
def f2(alpha, beta, gamma, point):
    rotations = np.dot(getRx(alpha), getRy(beta), getRz(gamma))
    return np.dot(rotations, point)


# 4) Test you rf2 with BP =[2,5,0] and α=30, β=90, γ=60.
pB = np.matrix([[2], [5], [0]])
f2(pi / 6, pi / 2, pi / 3, pB)






