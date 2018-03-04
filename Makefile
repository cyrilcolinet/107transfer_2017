##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

all:
	cat src/main.py > 107transfer
	echo -e "\n" >> 107transfer
	cat src/transfert_functions.py >> 107transfer
	chmod +x 107transfer

clean:
	rm -rf file

fclean: clean
	rm -rf 107transfer

re: fclean all
