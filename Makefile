##
## EPITECH PROJECT, 2018
## 107transfert_2017
## File description:
## Makefile
##

all:
	cat src/main.py > 107transfert
	echo -e "\n" >> 107transfert
	cat src/transfert_functions.py >> 107transfert
	chmod +x 107transfert

clean:

fclean: clean
	rm -rf 107transfert

re: fclean all
