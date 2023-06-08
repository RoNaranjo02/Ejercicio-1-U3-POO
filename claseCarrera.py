class Carrera:
    __cod = 0
    __nomb = None
    __fechaI = 0
    __duracion = None
    __titulo = None
    def __init__(self, cod = 0, nomb = None, fechaI = 0, duracion = 0, titulo = None):
        self.__cod = int(cod)
        self.__nomb = nomb
        self.__fechaI = int(fechaI)
        self.__duracion = int(duracion)
        self.__titulo = titulo
    def getcod(self):
        return self.__cod
    def getnomb(self):
        return self.__nomb
    def getfechaI(self):
        return self.__fechaI
    def getduracion(self):
        return self.__duracion
    def gettitulo(self):
        return self.__titulo

