import os
#from map_all import Map
from mapa_lectura import Mapa

def main():
    file = os.path.join('data', 'mapita.pdf')
    mapita = 'mapita.png'
    legend = 'leyendas.png'
    mapa = Mapa(mapita, legend)
    #mapa.turn_pdf(file)
    mapa.leyenda_colores()
    mapa.buscar_coordenada()

if __name__.endswith("__main__"):
    main()
