#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from matplotlib import pyplot as plt
from random     import shuffle
from math       import fsum
from timeit     import timeit

def time_exec(algo, l, nb):
	setup_str = 'from trisRapides import ' + algo + ' ; from listes import ' + l
	stmt_str = algo + '(' + l + '(' + str(nb) + '))'
	return timeit(setup = setup_str, stmt = stmt_str , number = 100)

def list_time_exec(algo, l, n_max):
	return [time_exec(algo, l, n) for n in range(1, n_max+1)]

def trace(algo, n_max):
	listes = ['cree_liste_croissante', 'cree_liste_decroissante', 'cree_liste_semi_melangee', 'cree_liste_melangee']
	size_l = len(listes)

	for lst in listes[::2]:
		y = list_time_exec(algo, lst, n_max)
		plt.plot(y, label = lst[5:10] + ' ' + lst[11:])

	shuffle(listes)
	durees = [None] * size_l 
	for id_lst, lst in enumerate(listes):
		durees[id_lst] = list_time_exec(algo, lst, n_max)
	# calcul du temps moyen sur les 4 listes choisies aléatoirement
	y = [fsum([durees[id_lst][i] for id_lst in range(size_l)])/size_l for i in range(n_max)] 
	plt.plot(y, label = 'liste ordre aléatoire')
	

if __name__ == '__main__':
	plt.xlabel('taille de la liste')
	plt.ylabel('temps d\'exécution en secondes')
	plt.subplot(121)
	plt.title('Tri rapide déterministe')
	trace('tri_rapide', 500)
	plt.grid()
	plt.legend()
	plt.subplot(122)
	plt.title('Tri rapide aléatoire')
	trace('tri_rapide_alea', 500)
	plt.grid()
	plt.legend()
	plt.show()
