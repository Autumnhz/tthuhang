# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 03:33:34 2024

@author: LAPTOP
"""

a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
if a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Nghiệm của phương trình là: ", -b/a)