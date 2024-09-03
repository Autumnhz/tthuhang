# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:09:21 2024

@author: LAPTOP
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))
min_number = a
if b < min_number:
   print("Số nhỏ nhất là: ",b)
elif c < min_number:
   print("Số nhỏ nhất là: ",c)
elif d < min_number:
   print("Số nhỏ nhất là: ",d)
else:
    print("Số nhỏ nhất là: ",a)
    

    
