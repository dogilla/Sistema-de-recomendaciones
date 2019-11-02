import csv
import random
import math
from numpy import linalg as la
import numpy

class Kmeans():
    """
    Una clase que representa el algoritmo de k-means y todos sus elementos.

    ...

    atributos
    ---------
    apps : list
        lista con todas las aplicaciones disponibles y sus datos, cada columna representa
        una app con los siguientes elementos en el mismo orden:
        [nombre, categoria, rating, instalaciones, tamaño, color]
    centroides: list of list
        lista que contiene los centroides (means) del algoritmo.
    num_colores : Int
        numero entero que representa el numero de colores en el algoritmo, es decir K
    colores: list of int
        lista con los colores que se le dan a los centroides y a los puntos en el plano,
        los colores son representados con enteros que van a de 0 a k.

    """

    apps = []
    centroides = []
    num_colores = 0
    colores = []

    def __init__(self, k_valor):
        self.open_document() #abre el documento
        self.nuevos_centroides(k_valor)
        self.num_colores = k_valor
        self.colores = [i for i in range(k_valor)]

    def open_document(self):
        """ 
        abre el documento csv y elimina las columnas con datos erroneos o que generan error, además
        transforma los elementos numericos de la aplicación a una representación de float.
        """

        with open('apps.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.apps.append(row)
        s = 0
        faltantes = [] 
        for app in self.apps:
            try:
                app[1] = float(app[1])
                app[2] = float(app[2])
                app[3] = float(app[3])
                app[4] = float(app[4])
            except:
                self.apps.pop(s)
                faltantes.append(s)
            finally:
                s = s +1
        for numero in faltantes:
            self.apps[numero][1] = float(self.apps[numero][1])
            self.apps[numero][2]  = float(self.apps[numero][2])
            self.apps[numero][3]  = float(self.apps[numero][3])
            self.apps[numero][4] = float(self.apps[numero][4])

                
    def nuevos_centroides(self, k):
        """  
        crea nuevos centroides con valores aleatorios dentro del espacio euclidiano de R4 
        """
        for i in range(k):
            categoria = random.randrange(33)
            rating = random.randrange(5)
            installs = random.randrange(10000)
            size = random.randrange(100)
            self.centroides.append([categoria,rating,installs,size])


    def distancia(self, a, b):
        """ 
        calcula la distancia entre dos vectores de R4, regresa el resultado redondeado a un float
        con 2 decimales
        """
        vector1 = numpy.array((a[0], a[1], a[2], a[3]))
        vector2 = numpy.array((b[0], b[1], b[2], b[3]))
        return round((numpy.linalg.norm(vector1-vector2)).item(), 2)


    
    def colorea_puntos(self):
        """
        colorea los puntos del espacio segun cual es el centroide más cercano, conceptualmente se 
        puede ver como la generacion de los clusters
        """
        for app in self.apps:
            dicc = {} #diccionario para poder devolver el resultado final
            i = 0
            for centroide in self.centroides:
                vector = [app[1],app[2],app[3],app[4]]
                dicc[self.distancia(vector, centroide)] = i #calcula de distacia de cada punto con su centroide
                i = i+1
            minimo = min(dicc.keys()) #regresa el minimo, el más cercano
            app[5] = dicc.get(minimo)
    
    def reajusta_centroides(self, centroides):
        """
        reajusta los centroides en el punto medio de todos los puntos del mismo color

        atributos
        ---------

        medias: list of list
            Una lista de listas, en donde cada lista interna guarda los valores de uno los atributos para 
            cada una de las apps que tienen el mismo color.

        resultados : list of float
            Lista que guarda el promedio (media aritmetica) de cada atributo que los apps que tienen el
            mismo color, esta lista se vuelve el nuevo centroide de ese color
        """
        medias = [[],[],[],[]]
        resultados = []
        for color in self.colores:
            for app in self.apps:
                if app[5] == color:
                    medias[0].append(app[1])
                    medias[1].append(app[2])
                    medias[2].append(app[3])
                    medias[3].append(app[4])
                else:
                    continue
            nuevo_centoide = []
            for media in len(medias):
                resultados.append(numpy.average(medias.pop()).item())
            self.centroides[color] = resultados
            resultados = []

    def k_mean_resulado(self):
        self.nuevos_centroides(73)
        
        


            









