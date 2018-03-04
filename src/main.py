#!/usr/bin/env python

##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Main file
##

import sys

if (__name__ == "__main__"):
	av = list(sys.argv);
	av.pop(0)
	if (len(av) == 0):
		print("Usage: ./107tranfert <num> <den>")
		exit(84)
	elif (len(av) == 1 and av[0] == "-h"):
		print("USAGE\n\t./107transfer <num> <den>*\n")
		print("\nDESCRIPTION\n\tnum\tpolynomial numerator defined ")
		print("by its coefs\n\tden\tpolynomial denominator defined by")
		print(" its coefs\n")
	elif (len(av) % 2 != 0):
		print("Usage: ./107tranfert <num> <den>")
		exit(84)
	elif (len(av) % 2 == 0 and len(av) > 0):
		transfert(av)
	else:
		print("Usage: ./107tranfert <num> <den>")
		exit(84)
	exit(0)
