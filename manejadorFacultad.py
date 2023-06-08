from claseFacultad import Facultad
from claseCarrera import Carrera
import csv
class Manejador:
    __lista = [[]]
    def __init__(self):
        self.__lista = [[]]
    def readFile(self):
        archivo = open("Facultades.csv")
        reader = csv.reader(archivo, delimiter = ",")
        for fila in reader:
            if int(fila[0])!=i:
			    self.__lista.append(Facultad(fila[0],fila[1],fila[2],fila[3],fila[4]))
				i=int(fila[0])
			else:
				self.__lista[i-1].agregarCarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
    def listar(self):
	    for facultad in self.__lista:
	        print(facultad)
		    facultad.mostrarCarreras()
    def mostrarCarrerasFacultad(self,i):
		i-=1
		self.__lista[i].mostrarCarreras()
    def buscarCarrera(self,carrera):
		for facu in self.__lista:
			facu.buscarCarrera(carrera)
                          
