# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 00:15:43 2021

@author: adria
"""

#Sesiones 3 y 4 de Python for Data Science
#Condiciones,bucles,POO,

#Conditions and Branching: Operadores de comparación == dev bool

a = 3; b = 6;
c = "HolaMundo"; d= "Python"
print(a != b);

print(a == b);

print(a > 5)
print (a < 5) 
print(b != 3) 
print(c != d)

#Branching: nos permite correr diferentes frases parad diferentes entradas
#IF 

if(a == 4) & (b == 5):
    print("hola")
print("adios")

#IF ELSE
edad = 19;

if(edad >= 18):
    print("Mayor de edad,entre.")
else:
    print("Menor de edad, salga.")
print("Buenos dias")

#ELSEIF

if(edad>18):
    print("entre")
elif(edad == 18):
    print("puede ir a ver Pink Floyd")
else:
    print("salga,menor de edad")
    
#Operadores Lógicos (not, or,)

not(True) == False
not(False) == True

achtung_baby = 1991;

album = achtung_baby;

if ((album >1990) or (album < 2000)):
    print("Album guardado")
else:
    print("album descartado")
    
#Operador and
if ((album >= 1990) and (album <= 2000)):
    print("Album guardado")
else:
    print("album descartado")
    
#Bucles
#Función range 
print(range(3)); #imprime 0,1,2
print(range(10,15))#imprime 10,11,12,13,14

#Bucle For
cuadrados = ["rojo","amarillo","verde","purpura","azul"];
long = len(cuadrados);

for i in range(5):
    print(cuadrados[i]+" sustituido por blanco")
    cuadrados[i] = "blanco";
    
print(cuadrados);
#rango reverso
for i in range(long-1,-1,-1):
    print(cuadrados[i]+" sustituido por verde")
    cuadrados[i] = "verde";
    
print(cuadrados);

for cuadrado in cuadrados:
    print(cuadrado);

#Bucle while

cuadrados2 = ["naranja","naranja","violeta","azul"];
cuadrados3=[]
i =0;

while(cuadrados2[i] == "naranja"):
    cuadrados3.append(cuadrados2[i]);
    i+=1;
    
print(cuadrados3);

#FUNCIONES PREDEFINIDAS
#len(), sorted(), sort();
#CREANDO NUESTRAS FUNCIONES

def add1(a):
    '''''
    primera funcion
    ejemplo explicatorio 
    '''''
    b=a+1;
    print(b);
    return b;

add1(5);

#Multiples parametros

def Mult(a,b):
    c=a*b;
    print(c);
    return c;

Mult(2,3);

#Funciones sin retorno devuelven objeto none
def MJ():
    print("Michael Jackson");
    
MJ();

#Python no permite cuerpo vacío, usamos "pass" como cuerpo (dev None)

#Colección de argumentos, pasar varios (asterisco)
def NombresArtistas(*nombres):
    for nombre in nombres:
        print(nombre);
        
NombresArtistas("Michael Jackson","U2","QUEEN");

#Scope de una variable: parte del programa donde es accesible.
#Si el valor no está definido en una función Python busca el global.
#Podemos crear variables locales usando la palabra "global nombrefuncion;"

