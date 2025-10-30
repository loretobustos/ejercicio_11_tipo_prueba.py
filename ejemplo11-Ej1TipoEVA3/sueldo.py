from empleado import Empleado

class Sueldo(Empleado):
    def __init__(self, id, apellidos, nombres, cargo, hrsContrato, estado, horario,
                 sueldoBase,bono,incentivo):
        super().__init__(id, apellidos, nombres, cargo, hrsContrato, estado, horario)
        self.sueldoBase=sueldoBase
        self.bono=bono
        self.incentivo=incentivo
    
    #def __str__(self) -> str:
    #    return super().__str__()
    
    def listarCargos(self,lista):
        cargo=input("Cargo a listar: ").upper()
        print("Las personas que cumplen el cargo de son:")
        sww=True
        for item in lista:
            if item.cargo.upper()==cargo:
                print("\t-",item.apellidos,", ",item.nombres)
                sww=False
        if sww:
            print("No hay personas que ejerzan el cargo de:",cargo)
    
    def listarJornadaManana(self,lista):
        listaJornada=[]
        for item in lista:
            if item.horario.jornada==1:
                listaJornada.append([item.apellidos,item.nombres])
                #print("\t-",item.apellidos,", ",item.nombres)
        return listaJornada
    
