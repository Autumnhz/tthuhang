# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:20:05 2024

@author: LAPTOP
"""

time1 = input("Nhập khoảng thời gian thứ nhất (giờ:phút:giây): ")
time2 = input("Nhập khoảng thời gian thứ hai (giờ:phút:giây): ")
h1, m1, s1 = map(int,time1.split(":"))
h2, m2, s2 = map(int,time2.split(":"))
if 0 <= h1 <= 23 and 0 <= m1 <= 59  and 0 <= s1 <= 59 and 0 <= h2 <= 23 and 0 <= m2 <= 59  and 0 <= s2 <= 59:
  sumgio = h1 + h2
  sumphut = m1 + m2
  sumgiay = s1 + s2
  print(f"Kết quả thời gian cộng: {sumgio}:{sumphut}:{sumgiay}")
  minusgio = h1 - h2
  minusphut = m1 - m2
  minusgiay = s1 - s2
  print(f"Kết quả thời gian trừ: {minusgio}:{minusphut}:{minusgiay}")
else:
    print("Không hợp lệ!")
