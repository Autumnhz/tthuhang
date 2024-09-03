# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:52:32 2024

@author: LAPTOP
"""

i = input("Nhập một chữ cái: ")
if i.islower():
    print("Kết quả sau khi chuyển đổi:", i.upper())
elif i.isupper():
    print("Kết quả sau khi chuyển đổi:", i.lower())
else:
    print("Không hợp lệ!")