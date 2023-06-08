from claseCarrera import Carrera
class Facultad:
    __codigo = 0
    __nombre = None
    __direc = None
    __localidad = None
    __tel = 0
    __listaCarreras = []
    def __init__(self, codigo = 0, nombre = None, direc = None, localidad = None, tel = 0, listaCarreras):
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__direc = int(direc)
        self.__localidad = localidad
        self.__tel = int(tel)
        for i in range(len(listaCarreras)):
            self.__listaCarreras.append(Carrera(listaCarreras[i][1]))
       

    def getcodigo(self):
        return self.__codigo
    def getnom(self):
        return self.__nombre
    def getdirec(self):
        return self.__direc
    def getlocal(self):
        return self.__localidad
    def gettel(self):
        return self.__tel
    def buscarCarrera(self,carrera):
	    carrera=carrera.lower()
	    i=0
		flag=False
		while not flag and i<len(self.__lista):
			if self.__lista[i].nombre()==carrera:
				print(f"{self.__codigo}.{self.__lista[i].codigo()}")
				print(self.__lista[i])
				print("Localidad: ",self.__localidad)
				flag=True
			else:
				i+=1    
    