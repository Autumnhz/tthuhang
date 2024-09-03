# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 03:53:24 2024

@author: LAPTOP
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
if 0 <=  h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
    print("Giờ, phút, giây hợp lệ.")
else:
    print("Không hợp lệ!")