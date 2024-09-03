# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:14:05 2024

@author: LAPTOP
"""

k = input("Nhập vào ký tự chữ thường: ")
if len(k) == 1 and k.islower():
    kth = k.upper()
    print("Ký tự chữ hoa tương ứng: ",kth)
else:
    print("Không hợp lệ!")