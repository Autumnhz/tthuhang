# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:14:29 2024

@author: LAPTOP
"""

t = input("Nhập thời gian theo định dạng (hh:mm:ss): ")
gio, phut, giay = map(int, t.split(":"))
g = gio * 3600 + phut * 60 + giay
print("Số giây:",g)
