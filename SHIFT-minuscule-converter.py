#!/usr/bin/env python3
#petamux2000.py

usuarioElc = int(input("""                Bienvenido a Petamux200 

                Que accion desea hacer?

MAYUSCULAS a minusculas(1) o minusculas a MAYUSCULAS(2)"""))




opcUsuario = [1, 2]




if usuarioElc == opcUsuario[0]:
    convert1 = input("Ingrese el texto a convertir: ")
    print(convert1.lower())

elif usuarioElc == opcUsuario[1]:
    convert2 = input("Ingrese el texto a convertir: ")
    print(convert2.upper())
