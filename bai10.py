# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:37:20 2024

@author: LAPTOP
"""

s = int(input("Nhập số xe có 4 chữ số: "))
if 1000 <= s <= 9999:
    t = sum(int(chu_so) for chu_so in str(s))
    s = t % 10
    print("Số nút của biển số xe là:", s)
else:
    print("Không hợp lệ!")