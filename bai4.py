# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:11:35 2024

@author: LAPTOP
"""

n = int(input("N = "))
if n >= 10 and n <= 99:
    pd = n%10
    pn = n//10
    S = pd + pn
    print("Kết quả:", S)
else:
    print("Không hợp lệ!")
    