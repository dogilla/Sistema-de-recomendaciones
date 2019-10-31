import csv
import random
import math
from numpy import linalg as la
import numpy

class Kmeans():
    """
    class:

    app:
        [nombre, categoria, rating, installs, size, color]
    """

    apps = []
    centroides = []
    num_colores = 0
    colores = []

    def __init__(self, k_valor):
        self.open_document() #lista de listas con los 6 elementos de cada app
        self.nuevos_centroides(k_valor)
        self.num_colores = k_valor
        self.colores = [i for i in range(k_valor)]

    def open_document(self):
        """ abre el documento """
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
        """  crea nuevos centroides con valores aleatorios dentro del espacio R4 """
        centroides = []
        for i in range(k):
            categoria = random.randrange(33)
            rating = random.randrange(5)
            installs = random.randrange(10000)
            size = random.randrange(100)
            self.centroides.append([categoria,rating,installs,size])


    def distancia(self, a, b):
        """ distancia entre 2 vectores de R4 """
        vector1 = numpy.array((a[0], a[1], a[2], a[3]))
        vector2 = numpy.array((b[0], b[1], b[2], b[3]))
        return round((numpy.linalg.norm(vector1-vector2)).item(), 1)


    
    def colorea_puntos(self):
        """
        colorea los puntos del espacio segun cual es el centroide más cercano
        """
        for app in self.apps:
            dicc = {}
            i = 0
            for centroide in self.centroides:
                vector = [app[1],app[2],app[3],app[4]]
                dicc[self.distancia(vector, centroide)] = i
                i = i+1
            minimo = min(dicc.keys())   
            app[5] = dicc.get(minimo)
    
    def ajusta_centroides(self, centroides):
        """
        reajusta los centroides en el punto medio de todos los puntos de dicho color
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
        
        


            









