# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:22:53 2024

@author: LAPTOP
"""

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
max_number = a
if b > max_number:
    print("Số có giá trị lớn nhất là: ",b)
elif c > max_number:
    print("Số có giá trị lớn nhất là: ",c)
else:
    print("Số có giá trị lớn nhất là: ",a)