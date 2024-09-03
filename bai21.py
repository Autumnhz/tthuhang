# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:33:24 2024

@author: LAPTOP
"""

chuoi_so = {
    0: "Không",
    1: "Một",
    2: "Hai",
    3: "Ba",
    4: "Bốn",
    5: "Năm",
    6: "Sáu",
    7: "Bảy",
    8: "Tám",
    9: "Chín"
    }
a = int(input("Nhập một số bất kỳ: "))
if 0 <= a <= 9:
    print("Thông báo:",chuoi_so[a])
else:
    print("Không đọc được.")