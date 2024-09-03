# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 03:46:43 2024

@author: LAPTOP
"""

import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
       x = -c / b
       print("Phương trình có 1 nghiệm x = ", x)
else:
    delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm!")
elif delta == 0:
    x= -b / (2 * a) 
    print("Phương trình có 1 nghiệm kép = ", x)
else:
    print("Phương trình có 2 nghiệm phân biệt!")
    x1= (-b + math.sqrt(delta)) / (2 * a)
    x2= (-b - math.sqrt(delta)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)