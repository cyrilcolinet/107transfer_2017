##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## 107transfert file
##

from sys import argv

def get_polynom(av):
	num = []
	try:
		for loop in range(len(av)):
			num.append(av[loop].split("*"))
		for loop in range(len(num)):
			for key in range(len(num[loop])):
				num[loop][key] = int(num[loop][key])
	except:
		exit(84)
	return (num)

def transfert(av):
	num = get_polynom(av)
	poly_one = 0
	poly_two = 0
	i = 0
	x = 0
	result = 0
	while (x <= 1.001):
		result = 1
		for i in range(0, len(num), 2):
			poly_one = 0
			poly_two = 0
			for j in range(len(num[i])):
				poly_one += (x ** j) * num[i][j]
			for k in range(len(num[i + 1])):
				poly_two += (x ** k) * num[i + 1][k]
			result *= poly_one / poly_two
		print("{0:g} -> {1:.5f}".format(x, result))
		x += 0.001

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
