#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from random_ex2 import *

def pseudo_premier_base(a, n):
	alpha, q = alpha_q(n)
	x = puissance(a, n-1, n)
	if x == 1:
		return True
	else:
		return False

for nb in range(3, 10000):
	if pseudo_premier_base(2, nb) and pseudo_premier_base(3, nb) and pseudo_premier_base(5, nb) and not naif(nb):
		print(nb)
		break
