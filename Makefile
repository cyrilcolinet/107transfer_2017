##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

all:
	cat src/107transfer.py > 107transfer
	chmod +x 107transfer

clean:
	rm -rf file

fclean: clean
	rm -rf 107transfer

re: fclean all
