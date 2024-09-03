# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 03:01:38 2024

@author: LAPTOP
"""

import math
h = input("Nhập hình (v, n hoặc t): ")
if h == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    cv = canh * 4
    print("Chu vi hình vuông là: ",cv)
    dt = canh * canh
    print("Diện tích hình vuông là: ",dt)
elif h == 'n':
    cr = float(input("Nhập chiều rộng hình chữ nhật: "))
    cd = float(input("Nhập chiều dài hình chữ nhật: "))
    cv = (cd + cr) * 2
    print("Chu vi hình chữ nhật là: ",cv)
    dt = cd * cr
    print("Diện tích hình chữ nhật là: ", dt)
elif h == 't':
    bk = float(input("Nhập bán kính đường tròn: "))
    cv = bk * math.pi * 2
    print("Chu vi hình tròn là: ", cv)
    dt = math.pi * (bk **2)
    print("Diện tích hình tròn là: ",dt)
else:
    print("Không hợp lệ!")
    
    
