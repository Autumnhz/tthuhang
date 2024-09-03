# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 04:00:48 2024

@author: LAPTOP
"""

h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
s = int(input("Nhập số giây: "))
t = h * 3600 + m * 60 + s
print("Tổng số giây là: ", t)