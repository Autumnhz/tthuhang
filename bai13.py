# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:22:30 2024

@author: LAPTOP
"""

d = int(input("Nhập ngày sinh: "))
m = int(input("Nhập tháng sinh: "))
y = int(input("Nhập năm sinh: "))
if 1 <= d <= 31 and 1 <= m <= 12:
    print("{}/{}/{}".format(d, m, y))
    print("{}/{}/{}".format(d, m, str(y)[-2:]))
    print("{}/{}/{}".format(y, m,d))
else:
    print("Không hợp lệ!")
#Làm ngược lại:
y = int(input("Nhập năm sinh: "))
m = int(input("Nhập tháng sinh: "))
d = int(input("Nhập ngày sinh: "))
if 1 <= d <= 31 and 1 <= m <= 12:
    print("{}/{}/{}".format(d, m, y))
    print("{}/{}/{}".format(d, m, str(y)[-2:]))
    print("{}/{}/{}".format(y, m,d))
else:
    print("Không hợp lệ!")
    