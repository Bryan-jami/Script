# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 09:29:11 2019

@author: Lalo
"""

from os import listdir

def ls(ruta = '.'):
    return listdir(ruta)

path = r'C:\Users\Lalo\Desktop\SIGNS BRYAN JAMI\EC_resp\SIGN_31\\'
lista = ls(r'C:\Users\Lalo\Desktop\SIGNS BRYAN JAMI\EC_resp\SIGN_31')

for n in lista:
    import csv
    time = 0.0
    with open(n, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Time', 'AccelX', 'AccelY', 'AccelZ', 'GiroX', 'GiroY', 'GiroZ'])
        
        with open(path+n, 'r', newline='') as incsv:
            reader = csv.reader(incsv)
            for row in reader:
                writer.writerow([time] + row)
                time = time + 0.2
                time = round(time,1)