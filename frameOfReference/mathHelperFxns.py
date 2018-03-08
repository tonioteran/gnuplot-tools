#!/usr/bin/python3

'''
Title: 		mathHelpersFxns.py
Author: 	Antonio Teran
Date:  		07/03/2018
Description:    Helper functions for quaternion/rot matrix transforms.
Usage:		Import the module into a main file.
'''

# Useful imports:
import numpy as np
import sys, os

def getQuatFromData(data,quatPos):
    '''
    Takes in a line of data, spits out a 4x1 numpy array
    Input: 	data - array, with data values from text file
    	     quatPos - int, position of first quaternion value
    Output:     quat - numpy array, [qx,qy,qz,qw]^T
    '''
    quat = np.array([[float(data[quatPos]), float(data[quatPos+1]), float(data[quatPos+2]), float(data[quatPos+3])]]).T
    return quat/np.linalg.norm(quat) # normalize before returning


def getRotMatrix(quat):
    '''
    Transforms quaternion vector into rotation matrix
    Input:        quat - numpy array, [qx,qy,qz,qw]^T
    Output:  rotMatrix - numpy matrix, rotation matrix
    '''
    qx = quat[0,0]; qy = quat[1,0]; qz = quat[2,0]; qw = quat[3,0];
    return np.matrix([[ qw**2 + qx**2 + qy**2 + qz**2, 2*(qx*qy - qw*qz), 2*(qx*qz + qw*qy) ],\
                      [ 2*(qx*qy + qw*qz), qw**2 - qx**2 + qy**2 - qz**2, 2*(qy*qz - qw*qx) ],\
                      [ 2*(qx*qz - qw*qy), 2*(qy*qz + qw*qx), qw**2 - qx**2 - qy**2 + qz**2]])
    

def getRotFramePoints(rotMatrix):
    '''
    Transforms the three unit vectors into the rotated frame
    Input:    rotMatrix - numpy matrix, rotation
    Output:    rotFrame - array, has three numpy arrays as elements (rotated endpoints of unit vectors)
    '''
    ux = np.array([[1,0,0]]).T; uy = np.array([[0,1,0]]).T; uz = np.array([[0,0,1]]).T;
    return [rotMatrix*ux, rotMatrix*uy, rotMatrix*uz]


    



