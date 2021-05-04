# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:49:10 2021

@author: adria
hola mundo
"""
#impresion
print("hola mundo");

#ejemplo 2
print("Hello\nWorld!")
#Tipos int float str 

#type casting (conversion tipos)
#float(2):2.0
#int('1'):1

#Expresiones: operaciones matematicas +,-,*,%,/,//(integer)
#Variables: my_variable = 1
var = 1;
print(var)
total_horas = 0;
total_min=0;

#Strings o Cadenas

Cadena = "IBM";

print(Cadena[0]+Cadena[2]);

print(Cadena[-3]+Cadena[-1]);

#print(Cadena.size());

#otro ejemplo
Cadena2 = "Michael Jackson";

#coger posiciones pares empezando por 0
print(Cadena2[::2]);
print(Cadena2[0:2]);
#Metodo Upper

A = "Achtung Baby mola";
B = A.upper();
print(B);

#Metodo replace

B= A.replace('Achtung Baby','The Joshua Tree');
print(B);

#Metodo find
donde = A.find("h");
print(donde);

#Longitud de la Cadena

cad = "hola";
print(len(cad));

#Listas y Tuplas (tuplas = inmutables, no podemos cambiarla, creamos otra)
#Tuples
notas =(10,9,8,7,6,5,3,2,1,);

#las tuplas pueden tener diferentes tipos dentro, su tipo es Tuple
Tupla1 = ("disco","Achtung Baby",5.99);
Tupla2 = Tupla1 + ("1"," Rock", "€");
#Concatenar adiciona más info
print(Tupla2[0:3]);
print(Tupla2[3:6]);

#Longitud tupla
print(len(Tupla2));
print(len(Tupla2[0:3]));

#Nesting o anidando tuplas
tuplaNested = ("pos1",(1,2),3,("pos4,pos5-1"));
print(len(tuplaNested));
print(tuplaNested[1]);
#sacando la primera pos de un doble elemento en nested
print(tuplaNested[1][0]);
#ordenar una tupla

tupla_des = (-1,0,-9,8,2);

tupla_ord = sorted(tupla_des);
print(tupla_ord);
#Listas.  No son inmutables. Permite nesting.Accesibles por index.Negat.Index

Lista1 = ["Tomate","Lechuga","Pasas","Vino"];
#imprimo los dos primeros elementos de la lista
print(Lista1[0:2]);
#imprimo los dos primeros elementos de la lista
print(Lista1[-4:-2]);
#concateno listas. Al ser mutable se modifca:
Lista2 = [1,2,3,4,5];
Lista2.extend([6,7]);
print(Lista2);

#Añadir un unico elemento a la lista (append)
Lista2.append([8,9,10]);
print(Lista2);

#Eliminar un elemento de la lista (elimino num 6)
del(Lista2[5]);
print(Lista2);

#Convertir String separado por espacios a Lista usando split()
str1 = "Celta de Vigo";
str2 = str1.split();
print(str2);

#Aliasing, cuando varios nombres referencian lo mismo
str4 = str1;
#si cambiamos algo en sr1 se verá afectado. Si queremos clonar:
str3 = str1[:]; #aqui creamos un clon o nueva instancia con valores str1

#Otro tipo de colecciones nueva: SETS
#son desordenados, solo tienen elementos únicos, no habrá duplicados al crear.
Set1 = {'Rock','Jazz','Pop','Opera'};
#convertir lista a set: set(Lista()) -> set
album_list = ["Achtung Baby","The Joshua Tree","Pop","Achtung Baby"];
print(album_list);
album_set = set(album_list);
print(album_set);

#Operacion de SET
#Añadir
album_set.add("Boy");
print(album_set);

#eliminar (remove)
album_set.remove("Pop");
print(album_set);

#Operaciones matemáticas en SET
album_set2 = {'Achtung Baby',"Thriller","Meteora"};

#Intersección usamos & (lo q esta en los dos sets)

inter_set = album_set & album_set2;
print(inter_set); 

#Union de dos sets (cogemos todo) usamos 


#DICCIONARIOS
#Par clave-valor.Clave = index pero no tiene que ser int.
#Claves inmutables/unicas
#Valores pueden ser mutables o inmutables, repetidos...
#primer termino clave segundo valor.
diccio1 = {"Achtung Baby":1991,"Zooropa":1993,"Pop":1997};

#añadiendo valores al diccionario (por clave)
diccio1['ATYCLB'] = 2000;
print(diccio1);

#eliminando valores del diccionario (por clave)
del(diccio1["Achtung Baby"])

#comprobando valores del diccionario (dev true o false)
print("war" in diccio1);

#ver todas las claves que contiene un diccionario
print(diccio1.keys());

#Obtener todos los valores que tiene un diccionario
print(diccio1.values());


