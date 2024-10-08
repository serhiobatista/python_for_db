# Дан список из чисел.
# Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель).

from math import gcd, lcm
from functools import reduce


def find_gcd(*kwargs):
    x = reduce(gcd, kwargs)
    return x


def find_lcm(*kwargs):
    x = reduce(lcm, kwargs)
    return x

