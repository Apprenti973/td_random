#! /usr/bin/python3.6
# coding: utf-8

__author__ = "Derrien Tanguy"

from random_ex2 import *

# test de Miller pour n = 121 et base = 3
print(test_Miller_Rabin(121, 3, alpha_q(121)[0], alpha_q(121)[1]))

# test de Miller pour n = 781 et base = 5
print(test_Miller_Rabin(781, 5, alpha_q(781)[0], alpha_q(781)[1]))

# version probabiliste avec 100 essais
print(premier_Miller_Rabin(121, 100))
print(premier_Miller_Rabin(781, 100))
