#!/usr/bin/python3

'''
Title: 		dataParser.py
Author: 	Antonio Teran
Date:  		07/03/2018
Description:    Script for reading in data files with orientation info,
		and appending frame of reference information for gnuplot.
Usage:		$ ./dataParser.py pathAndNameOfDataFile [separatorCharacter]
		Parameters:
			- pathAndNameOfDataFile: string, name of file. e.g., dataFile.dat
			- numberOfObjects:       integer, number of trajectories/objects to plot
			For each object:
				- quaternionColumn:      integer, column in which the orientation data starts
				- positionColumn:        integer, column in which the position data starts
			- [separatorCharacter]:  char (optional). ',' (comma) by default.
'''

# Useful imports:
import numpy as np
import sys, os, time

# Custom imports:
from mathHelperFxns import getScaledFrame

# Parameters:
FRAME_LENGTH = 0.3

status = True; localTime = time.localtime();
# Check for included arguments:
if len(sys.argv) < 5:
    print('\n*********\nNOT ENOUGH ARGUMENTS\nPlease see usage.\n')
    status = False
elif len(sys.argv) == (3 + int(sys.argv[2])*2):
    separatorChar = ',' # default value
    numOfObjs = int(sys.argv[2])
    posIndices = []
    quatIndices = []
    for obj in range(numOfObjs):
        quatIndices.append( int(sys.argv[3 + 2*obj]) )
        posIndices.append(  int(sys.argv[4 + 2*obj]) )
    datafile = open(sys.argv[1], 'r') # just read the file; no modifications to original
elif len(sys.argv) == (3 + int(sys.argv[2])*2 + 1):
    separatorChar = str(sys.argv[-1]) # set user defined value
    numOfObjs = int(sys.argv[2])
    posIndices = []
    quatIndices = []
    for obj in range(numOfObjs):
        quatIndices.append( int(sys.argv[3 + 2*obj]) )
        posIndices.append(  int(sys.argv[4 + 2*obj]) )
    datafile = open(sys.argv[1], 'r') # just read the file; no modifications to original
else:
    print('\n\n*********************')
    print('Stopping! Provided ' + str(len(sys.argv)) + ' arguments. With ' + str(sys.argv[2]) + ' objs, you need...')
    print('Usage: $ ./' + str(sys.argv[0]) + 'pathAndNameOfDataFile [separatorCharacter]')
    print('Try again\n\n')
    status = False

if status:
    outputfilename = 'outFileWithFrames_' + str(localTime.tm_hour) + '-' + str(localTime.tm_min) + '-' + str(localTime.tm_sec) + '.dat'
    outputfile = open(outputfilename, 'w')
    outputfile.write('# Augmented data file with coordinate frame info.')
    # Iterate over each datafile line, and write out augmented data file:
    for line in datafile:
        if line[0] != '#':
            tempData = line.split(separatorChar) 		# Split line into values
            tempData[-1] = tempData[-1].split('\n')[0]		# Get rid of the new line
            scaledFrames = []
            for obj in range(numOfObjs):
                scaledFrames.append( getScaledFrame(tempData,quatIndices[obj],FRAME_LENGTH) )
            outputfile.write('\n')
            # Write data to output file:
            for i,e in enumerate(tempData):
                if i != 0:
                    outputfile.write(', ')
                outputfile.write(e)
            for obj in range(numOfObjs):
                for p in scaledFrames[obj]:
                    for i in range(len(p)):
                        outputfile.write(', ')
                        outputfile.write(str(p[i,0]))

            
            print(tempData)
            print('------')
            
    datafile.close()
    outputfile.close()
# end

