import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure
from pdf2image import convert_from_path

class Mapa():
    def __init__(self, pathfile, pathlegend):
        self.mapa = io.imread(pathfile)
        self.leyenda = io.imread(pathlegend)

    def turn_pdf(self, file):
        pages = convert_from_path(file)
        for page in pages:
            page.save('outmapita.jpg', 'JPEG')

    def leyenda_colores(self):
        self.colores = []
        self.leyenda = color.rgb2gray(self.leyenda)
        #io.imshow(self.leyenda)
        #plt.show()
        #print(np.shape(self.leyenda)[0])
        #print(self.leyenda)
        for i in range(np.shape(self.leyenda)[0]):
            for j in range(np.shape(self.leyenda)[1]):
                #print(self.leyenda[i, j])
                if (self.leyenda[i, j]) not in self.colores and (self.leyenda[i, j] != 1):
                    self.colores.append(self.leyenda[i, j])

        #niveles = ['1', '2', '3', '4']

        print(self.colores)

    def buscar_coordenada(self):
        mapita = color.rgb2gray(self.mapa)
        #io.imshow(mapita)
        #plt.show()
        puntos = []
        found = 0
        # Punto arriba
        for i in range(np.shape(mapita)[0]):
            for j in range(np.shape(mapita)[1]):
                if mapita[i, j] in self.colores:
                    found = 1
                    puntos.append((i, j))
                    break
            if found == 1:
                break

        found = 0
        # Punto izquierda
        for i in range(np.shape(mapita)[1]):
            for j in range(np.shape(mapita)[0]):
                if mapita[j, i] in self.colores:
                    found = 1
                    puntos.append((j, i))
                    break
            if found == 1:
                break
        found = 0
        # Punto abajo
        filas = np.shape(mapita)[0]
        for i in range(filas):
            for j in range(np.shape(mapita)[1]):
                if mapita[filas-i-1, j] in self.colores:
                    found = 1
                    puntos.append((filas-i-1, j))
                    break
            if found == 1:
                break
        found = 0
        # Punto derecha
        columnas = np.shape(mapita)[1]
        for i in range(np.shape(mapita)[1]):
            for j in range(np.shape(mapita)[0]):
                if mapita[j, columnas-i-1] in self.colores:
                    print('hol')
                    found = 1
                    puntos.append((j, columnas-i-1))
                    break
            if found == 1:
                break
        coor = {'sup': puntos[0][0], 'izq': puntos[1][1], 'aba': puntos[2][0], 'der': puntos[3][1]}
        #recortes = [(coor['sup'], coor['izq']), (coor['aba'], coor['izq']),
        #            (coor['inf'], coor['der']), (coor['sup'], coor['der'])]
        print(puntos)

        nuevo_mapa = mapita[coor['sup']: coor['aba'], coor['izq']:coor['der']]
        shape_mapa = np.shape(nuevo_mapa)
        print(shape_mapa)
        # Hallar pixel en y
        rango_y = [12, -4]
        rango_x = [-66.86, -79]
        m1 = shape_mapa[0]/sum([rango_y[0], -rango_y[1]])
        b1 = -m1*rango_y[1]
        print(m1, b1)
        y = round(m1*6 + b1)-1
        print(y)
        m2 = shape_mapa[1]/sum([rango_x[0], -rango_x[1]])
        b2 = - m2*rango_x[1]
        print(m2, b2)
        x = round(m2*-70+b2)-1
        print(y, x)
        print(nuevo_mapa[y, x])

        #io.imshow(nuevo_mapa)
        #plt.show()
