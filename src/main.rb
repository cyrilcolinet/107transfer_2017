##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## main file
##

require "src/transfer"

av = ARGV
av.pop(0)

if av.size == 0
	print("Usage: ./107transfer <num> <den>")
	Kernel.exit(false)
elsif av.size == 1 && av[0] == "-h"
	print("USAGE\n\t./107transfer <num> <den>*\n")
	print("DESCRIPTION\n\tnum\tpolynomial numerator defined by its coefficients")
	print("\tden\tpolynomial denominator defined by its coefficients")
	Kernel.exit(true)
elsif av.size > 0 && av.size % 2 == 0
	transfer = Transfer.new(av)
	transfer.execute()
else
	print("Usage: ./107transfer <num> <den>")
	Kernel.exit(false)
end
