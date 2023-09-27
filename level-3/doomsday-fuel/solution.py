from __future__ import division
from fractions import Fraction, gcd
from copy import deepcopy


def solution(m):
    values = transition_matrix(m)
    if type(values) is tuple:
        m, a, b = values
    else:
        terminal = values
        return [1] + [0] * (len(terminal) - 1) + [1]
    f = inverse(subtract(identity(len(b)), b))
    s = multiply(f, a)
    denom = reduce(lcm, (frac.denominator for frac in s[0]))
    num = [frac.numerator * denom // frac.denominator for frac in s[0]]
    return num + [denom]


def transition_matrix(m):
    terminal = []
    for i, row in enumerate(m):
        if all(not x for x in row):
            terminal.append(i)
    if 0 in terminal:
        return terminal
    t = transpose(m)
    for i, row_i in enumerate(reversed(terminal)):
        t[-i - 1], t[row_i] = t[row_i], t[-i - 1]
    n = transpose(t)
    for i, row_i in enumerate(reversed(terminal)):
        n[-i - 1], n[row_i] = n[row_i], n[-i - 1]
    for i in range(len(m) - 1, len(m) - len(terminal) - 1, -1):
        n[i][i] = 1
    for i, row in enumerate(n):
        s = sum(row)
        n[i] = [Fraction(x, s) for x in row]
    a = deepcopy(n)
    a = [row[-len(terminal) :] for row in a[: -len(terminal)]]
    b = deepcopy(n)
    b = [row[: -len(terminal)] for row in b[: -len(terminal)]]
    return n, a, b


def lcm(a, b):
    return a * b // gcd(a, b)


def transpose(m):
    m = deepcopy(m)
    return [list(x) for x in zip(*m)]


def subtract(m, n):
    return [[m[i][j] - n[i][j] for j, _ in enumerate(row)] for i, row in enumerate(m)]


def multiply(m, n):
    t = transpose(n)
    return [[sum(a * b for a, b in zip(row, col)) for col in t] for row in m]


def inverse(m):
    m = deepcopy(m)
    n = identity(len(m))
    a = [a + b for a, b in zip(m, n)]
    a = gaussian_elimination(a)
    return [row[len(row) // 2 :] for row in a]


def identity(n):
    return [[Fraction(0)] * i + [Fraction(1)] + [Fraction(0)] * (n - i - 1) for i in range(n)]


def gaussian_elimination(m):
    m = deepcopy(m)
    l = len(m)
    for i in range(l):
        if not m[i][i]:
            for j in range(i + 1, l):
                if m[j][i]:
                    m[i], m[j] = m[j], m[i]
        for j in range(i + 1, l):
            m = eliminate(m, i, j, i)
    for i in range(l - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            m = eliminate(m, i, j, i)
    for i in range(l):
        m = eliminate(m, i, i, i, target=1)
    return m


def eliminate(m, i, j, col, target=0):
    m = deepcopy(m)
    factor = (m[j][col] - target) / m[i][col]
    for k in range(len(m[i])):
        m[j][k] -= factor * m[i][k]
    return m
