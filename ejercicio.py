#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd","r");
lineas = fd.readlines()
fd.close()

for linea in lineas:
    if not linea:
        break
    corte = linea.split(':')
    login = corte[0] 
    shell = corte[-1]
    print login, shell[:-1]
    
   
