# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:03:51 2024

@author: LAPTOP
"""

#(a) Cho ba số a, b, c được nhập vào từ bàn phím. Hãy in ra màn hình theo thứ tự tăng dần các số (Chỉ dùng 1 biến phụ).
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
s = [a, b, c]
sx = sorted(s)
print("Thứ tự tăng dần các số:",sx)
#(b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần.
n = int(input("Nhập vào một số nguyên N: "))
n = str(n)
sx = sorted(n)
print("Số theo thứ tự tăng dần:",''.join(sx))