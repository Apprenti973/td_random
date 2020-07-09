#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from matplotlib           import pyplot    as plt
from random_ex2_question4 import time_exec 

indices = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217]

mersenne = list(map(lambda n : 2**n-1, indices))

Mi = list(map(lambda n : 'M' + str(n), indices))

y = list(map(lambda n : time_exec('premier_Miller_Rabin', n, ', 10'), mersenne))
plt.plot(y)

plt.xticks(range(len(indices)), Mi, rotation = 90)
plt.yticks([time for time in y if time > 1.3])
plt.title('Temps d\'exécution de l\'algorithme randomisé de Miller-Rabin (k = 10) sur les 19 premiers nombres premiers de Mersenne')
plt.ylabel('temps d\'exécution en secondes')
plt.grid()
plt.show()
