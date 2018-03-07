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
			- quaternionColumn:      integer, column in which the orientation data starts
			- positionColumn:        integer, column in which the position data starts
			- [separatorCharacter]:  char (optional). ',' (comma) by default.
'''

# Useful imports:
import numpy as np
import sys, os

# Check for included arguments:
if len(sys.argv) == 3:
    separatorChar = ',' # set default value
    quatColumn = int(sys.argv[2])
    posColumn = int(sys.argv[3])
    datafile = open(sys.argv[1], 'r') # just read the file; no modifications to original
elif len(sys.argv) == 4:
    separatorChar = str(sys.argv[4])  # set user defined value
    quatColumn = int(sys.argv[2])     # starting orientation column
    posColumn = int(sys.argv[3])      # starting position column
    datafile = open(sys.argv[1], 'r') # just read the file; no modifications to original
else:
    print('\n\n*********************')
    print('Stopping! Provided ' + str(len(sys.argv)) + ' arguments, while 2 or 3 are needed.')
    print('Usage: $ ./' str(sys.argv[0]) + 'pathAndNameOfDataFile [separatorCharacter]')
    print('Try again\n\n')

# Iterate over each datafile line, and write out augmented data file:
for line in datafile:
    print(line, end='')







# end
return 0
