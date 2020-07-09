#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from math   import sqrt
from random import randint

def naif(n):
	"""
	Algorithme naïf qui détermine si n est un nombre premier
	Entree :
	n : entier
	Sortie :
	res = (True | False)
	"""
	res = True
	
	# cas n = 0 et n = 1
	if n < 2:
		res = False
	
	# le cas 2 correspond à la valeur de res par défaut (True) car comme
	# sqrt(2)+1 = 2, la fonction renverrait un faux négatif
	
	# n > 2
	elif n > 2:
		# si n est pair et strictement supérieur à 2, il n'est pas premier
		if not n % 2:
			return False
		# on essaye de trouver un diviseur < sqrt(n)
		# 2 a déjà été testé donc inutile de tester les diviseurs pairs
		for essai in range(3, int(sqrt(n))+2, 2):
			if not n % essai:
				res = False
	return res


def alpha_q(n):
	"""
	Renvoie les entiers alpha et q tels que n - 1 = 2^alpha x q
	Entree :
	n : entier impair (donc n >= 3) à factoriser
	Sortie :
	alpha, q : tupple d'entiers
	Pour gagner en temps d'exécution lorsque n est un grand nombre,	on travaille
	directement sur l'écriture binaire de n. Pour diviser n par 2, on décale son
	écriture binaire de 1 bit vers la droite. Pour vérifier qu'il est pair, on
	compare son lsb à 0.
	"""
	# comme n est impair, n-1 est pair. Donc alpha >= 1 et q >= n-1 // 2
	alpha, q = 1, n-1 >> 1 

	# on décale de 1 bit vers la droite jusqu'à ce que le lsb de q soit égal à 1
	while not q & 1:
		alpha, q = alpha + 1, q >> 1
	return alpha, q 


def puissance(b, e, n):
	"""
	Calcule b^e [n] en utilisant la décomposition de e en base 2
	Entree :
	b, e, n : entier, entier, entier
	Sortie :
	res : entier
	"""
	res = 1
	while e > 0:
		if e & 1:
			res = (res * b) % n
		e = e >> 1
		b = (b * b) % n
	return res


def test_Miller_Rabin(n, x, alpha, q):
	"""
	Vérifie que x est un témoin de Miller pour le nombre n. Autrement dit :
	n étant un nombre impair tel que n = 2^alpha * q, x doit vérifier :
	1-- x^q != 1 [n] ou x^q != n-1 [n] (car -1 = n-1-n = n-1 [n])
	2-- Pour tout i de [0..alpha-1] (x^q)^(2^i) != n-1 [n]
	Entree :
	n : entier impair
	x : entier strictement inférieur à n (donc x non divisible par n)
	alpha : entier
	q : entier
	Sortie :
	True  : x est un témoin de Miller et n n'est pas premier
	False : x n'est pas un témoin de Miller
	"""

	# pour les grands nombres, l'exponentiation rapide modulaire est plus
	# efficace que la fonction pow
	t = puissance(x, q, n)
	
	# Condition 1
	if t == 1 or t == n-1:
		# x n'est pas un témoin de Miller
		return False
	
	# Condition 2
	for i in range(alpha):
		t = (t * t) % n
		if t == n-1:
			# x n'est pas un témoin de Miller
			return False
	
	# x est un témoin de Miller et n n'est pas premier
	return True


def premier_Miller_Rabin(n, k):
	"""
	Renvoie True si n est pseudo premier et False si n est composé. Dans ce cas,
	un témoin de Miller et la décomposition 2^alpha * q est également renvoyée
	Entree :
	n : entier ==> nombre à tester
	k : entier ==> k tests de Miller pour chercher des témoins de non primalité
	Sortie :
	(True | False, x, alpha, q)
	"""
	# Calcul de alpha et de q tels que n-1 = 2^alpha x q
	alpha, q = alpha_q(n)

	# on renouvelle le test k fois pour réduire la probabilité d'erreur
	for iter in range(1, k+1):
		
		# x < n et donc x non divisible par n
		x = randint(2, n)
		
		if test_Miller_Rabin(n, x, alpha, q):
			return False, x, alpha, q
	
	return True
