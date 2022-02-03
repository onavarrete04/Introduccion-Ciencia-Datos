# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

arreglo = np.array([1,2,3,4,5,6])

# arange genera un arreglo en numpy

arreglo = np.arange(1,7)

print(arreglo)

arreglo = np.array([1,2,3,4,5,6], dtype="i")

print(arreglo, arreglo.dtype,arreglo.itemsize)

arreglo = np.array([1,2,3,4,5,6], dtype="i2")

print(arreglo, arreglo.dtype,arreglo.itemsize)

arreglo = np.array([1,2,3,4,5,6], dtype="i4")

print(arreglo, arreglo.dtype,arreglo.itemsize)

arreglo = np.array([1,2,3,4,5,6], dtype="i8")

print(arreglo, arreglo.dtype,arreglo.itemsize)


