# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:38:17 2021
Abriendo archivos y leyendo - empezando con datos
@author: adria
"""

#Vamos a usar la instrucción "open" para abrir archivos
# Archivo = open("ruta absoluta.txt","w"); 
# w = writting, r = reading,a = appending;
#Archivo será tratado como un objeto, pudiendo usar sus metodos como .name

# es necesario: Archivo.name 'ruta'; Archivo.mode 'r'; Archivo.close();
# siempre debemos cerrar el archivo usando .close();

#forma ideal, hace lo identado y cierra archivo:
    
with open("C:/Archivo1.txt","r") as Archivo1:
    contenido = Archivo1.read();
    print(contenido);

print(Archivo1.closed); #chequeamos si cerraado
print(contenido);

#para leer listas usamos archivo = Archivo.readlines();

with open("C:/Archivo 2.txt","r") as Archivo2:
    contenido = Archivo2.readline();
    print(contenido);
    contenido = Archivo2.readline();
    print(contenido);

print(Archivo2.closed); #chequeamos si cerraado

#leer todo el archivo

with open("C:/Archivo 2.txt","r") as Archivo2:
    contenido = Archivo2.readlines();
    for i in contenido:
        print(i);
print(Archivo2.closed); #chequeamos si cerraado

#leer unos cuántos caracteres

with open("C:/Archivo 2.txt","r") as Archivo2:
    contenido = Archivo2.readlines(4);
    print(contenido);
    contenido = Archivo2.readlines(1);
    print(contenido);
print(Archivo2.closed); #chequeamos si cerraado

#Escribiendo archivos con open, usando argumento "r"

Archivo = open("C:/Users/adria/Archivo.txt","w")
Archivo.write("CRTs volveran\n");
Archivo.write("CRTs no volveran\n");

#Copiando el contenido de un archivo en otro nuevo
'''
with open("Ejemplo1.txt","r") as lectura:
    with open("Ejemplo2.txt","w") as escritura:
        for i in lectura:
            escritura.write(i);
 '''           
            
#CARGANDO DATOS CON PANDAS
import numpy as np;
import pandas as pd;

csv_path ='C:/Users/adria/Desktop/Archivo1.csv';
df1 = pd.read_csv(csv_path);

#CARGANDO DATOS EXCEL 
xlsx_path = "C:/Users/adria/Desktop/Archivo1.xlsx"
df2 = pd.read_excel(xlsx_path)

#De CSV o excel a Dataframes
df1.head(); #mirar por qué no va
df2.head();

#CREANDO NUESTROS PROPIOS DATAFRAMES
#CASTEAMOS DICCIONARIO A DATAFRAME

lista = {'Album':['Achtung Baby','Zooropa','War','Mutter'],'Ano':[1991,1993,1983,2001],'Cantante':['U2','U2','U2','Rammstein']};

lista_frame = pd.DataFrame(lista); #casteamos usando Pandas de dicc a DF

#CREAR NUEVO DATAFRAME A PARTIR DE COLUMNA (varias igual pero con comas)

x = lista_frame[['Album']];

#Accediendo a elementos en pandas
#MÉTODO IX // ahora .iloc, ix deprecated
#1º Fila 1º Columna:
print(lista_frame.iloc[0,0]);
print(lista_frame.iloc[0,1]);
print(lista_frame.iloc[1,0]);

z = lista_frame.iloc[0:2, 0:3];
print(z);


#TRABAJANDO CON DATOS GUARDADOS
#LISTA CON VALORES UNICOS
#Saber cuantos unicos hay en columna "Cantante"
print(lista_frame['Cantante'].unique());

#Trabajando con datos: discos de después del 2000 (ojo trabaja bools)
print(lista_frame['Ano']>=2000);

#Guardar a .csv
#fichaguardar.to_csv('nuevo_fichaguardar.csv');