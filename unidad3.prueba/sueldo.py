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
       