##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## tranfert_functions file
##

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
	return num

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
