from empleado import Empleado

class Sueldo(Empleado):
    def __init__(self, id, apellidos, nombres, cargo, estado, horasContrato, horario, sueldoBase, bono, insentivo):
        super().__init__()
        self.sueldoBase=sueldoBase
        self.bono=bono
        self.insentivo=insentivo

    def mostrarSueldo(self):
        print("Datos del Sueldo")
        print("Suelde Base       :",self.sueldoBase)
        print("Bono              :",self.bono)
        print("Motivo            :",self.motivo)

    def __str__(self) -> str:
        return super().__str__()

    def listaCargo(self, lista):
        cargo=input("Cargo a listar: ").ipper()
        print("Las personas que cumplen el cargo son: ")
        sww=True
        for item in lista: 
            if item.cargo.upper()==cargo:
                print("\t-",item.apellidos,", ",item.nombres)
                sww=False
        if sww:
            print("No hay personas que ejerzan ese cargo", cargo)


    def listarJornadaManana(self, lista):
        listaJornada=[]
        for item in lista:
            if item.horario.jornada==1:
                listaJornada.append([item.apellidos,item.nombres])
                print("\t-",item.apellidos,",",item.nombres)
        return listaJornada
