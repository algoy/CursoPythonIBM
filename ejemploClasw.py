# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:25:09 2021
#OBJETOS Y CLASES
@author: adria
"""

class Circle(object):#definimos la clase
    def _init_(self,radius,color):#atributos usados para inicializar
        self.radius = radius; #constructor definido en _init_
        self.color = color; #self no es atrib, radius y color si
        

#creamos un objeto

c1 = Circle(10,"red");      

#Manejando los atributos directamente ( se debe hacer en métodos)
c1.color = "green";

#Métodos: Ejemplo método ampliar radio
class Circle(object):#definimos la clase
    def _init_(self,radius,color):#atributos usados para inicializar
        self.radius = radius; #constructor definido en _init_
        self.color = color; #self no es atrib, radius y color si
   
    def add_radius(self,r):
        self.radius = self.radius + r;
        
        return(self.radius);
    
    c1.drawCircle();
    
#dir(nombreObjeto); nos da info de los métodos o atributos del objeto. 