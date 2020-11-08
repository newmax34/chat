# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:44:20 2020

@author: littl
"""


lines = []
with open ("3.txt", "r", encoding='utf-8-sig')as f:
    for line in f:
        lines.append(line.strip())
        
for line in lines: 
    s = line.split(" ")
    time = s[0][:5]
    name = s[0][5:]
    content = s[1:]
    print(time, "-", name, ":", content)



