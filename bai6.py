# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:48:57 2024

@author: LAPTOP
"""

import datetime
y = int(input("Vui lòng nhập năm sinh: "))
nam_hien_tai = datetime.datetime.now().year
t = nam_hien_tai - y
print(f"Bạn sinh năm {y} vậy bạn {t} tuổi.")
