#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from timeit     import timeit
from matplotlib import pyplot as plt


def time_exec(algo, n, k = ''):
	setup_str = 'from random_ex2_question1 import naif, premier_Miller_Rabin'
	stmt_str = algo + '(' + str(n) + k + ')'
	return timeit(setup = setup_str, stmt = stmt_str , number = 100)


def list_time_exec(algo, n_max, k = ''):
	return [time_exec(algo, n, k) for n in range(3, n_max+1, 2)]


def trace(n_max, k):
	x = list(range(3, n_max+1, 2))	
	plt.subplot(121)
	y = list_time_exec('naif', n_max)
	plt.xticks([3] + [n for n in range(0, n_max+1, 2) if not n%100 and n])
	plt.plot(x, y, label = 'algorithme naïf')
	plt.title('Temps d\'exécution de l\'algorithme naïf\npour les entiers impairs compris entre 3 et n_max')
	plt.xlabel('n_max')
	plt.ylabel('temps d\'exécution en secondes')

	plt.subplot(122)
	y = list_time_exec('premier_Miller_Rabin', n_max, ', 100')
	plt.xticks([3] + [n for n in range(0, n_max+1, 2) if not n%100 and n])
	plt.plot(x, y, label = 'algorithme de Miller-Rabin')
	plt.title('Temps d\'exécution du test de Miller Rabin\npour les entiers impairs compris entre 3 et n_max')
	plt.xlabel('n_max')
	plt.ylabel('temps d\'exécution en secondes')


if __name__ == '__main__':
	trace(1000, ', 10')
	plt.grid()
	plt.show()
