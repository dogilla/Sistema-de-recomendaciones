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
    n_apps: int
        numero de aplicaciones que hay en la base de datos

    """

    apps = []
    n_apps = 0
    centroides = []
    num_colores = 0
    colores = []

    def __init__(self, k_valor):
        self.open_document() #abre el documento
        self.nuevos_centroides(k_valor)
        self.num_colores = k_valor
        self.colores = [i for i in range(k_valor)]
        self.n_apps = len(self.apps)
        self.colorea_puntos()

    def open_document(self):
        """ 
        abre el documento csv y elimina las columnas con datos erroneos o que generan error, además
        transforma los elementos numericos de la aplicación a una representación de float.
        """

        with open('apps.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.apps.append(row)
        print(str(self.apps))
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
    
    def reajusta_centroides(self):
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
        medias = [[0],[0],[0],[0]]
        resultados = []
        for color in self.colores:
            for app in self.apps:
                if app[5] == color:
                    medias[0][0] = medias[0][0] + app[1]
                    medias[1][0] = medias[1][0] + app[2]
                    medias[2][0] = medias[2][0] + app[3]
                    medias[3][0] = medias[3][0] + app[4]
                else:
                    pass
            m = lambda x : round((x/self.n_apps),1)
            resultados = [m(i[0]) for i in medias]
            self.centroides[color] = resultados
            resultados = []

    def k_mean_resultado(self, aplicacion):
        """
        devuelve una lista con los resultados de la recomendacion
        """
        viejo_centroide = self.centroides[1]
        nuevo_centroide = []
        while (viejo_centroide != nuevo_centroide):
            viejo_centroide = self.centroides[1]
            self.reajusta_centroides()
            nuevo_centroide = self.centroides[1]
            self.colorea_puntos()

        resultados = []
        for app in self.apps:
            if app[0] == aplicacion:
                c = app[1]
                color_app = app[5]
                break
        for app in self.apps:
            if app[5] == color_app and app[1] == c:
                resultados.append(app[0])
        return resultados

        

        
        


            









