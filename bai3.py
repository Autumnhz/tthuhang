# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:00:04 2024

@author: LAPTOP
"""

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if a > 0 and b > 0:
   c = a%b
   print ("Chia lấy dư: a:b =", c)
   d = a//b
   print("Chia lấy nguyên: a:b =", d)
else:
    print("Không hợp lệ!")
