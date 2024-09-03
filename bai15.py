# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 03:25:34 2024

@author: LAPTOP
"""

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
A = a + b
B = a ** (1/3) + b ** (1/3)
C = (a*b) ** (1/3)
D = (a ** (1/3) - b ** (1/3)) ** 2
k = ((A/B)- C) / D
print("Kết quả: ",k)