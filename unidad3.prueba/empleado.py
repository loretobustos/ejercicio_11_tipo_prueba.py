class Empleado():
    def __init__(self, id, apellidos, nombres, cargo, estado, horasContrato, horario):
        self.id=id
        self.apellidos=apellidos
        self.nombres=nombres
        self.cargo=cargo
        self.estado=estado
        self.horaContrato=horasContrato
        self.horario=horario   #es la instancia de emleado a horario

    def mostrarEmpleado(self):
        print("Datos del empleado")
        print("ID           :",self.id)
        print("Apellidos    :",self.apellidos)
        print("Nombres      :",self.nombres)
        print("Cargo        :",self.cargo)
        print("Estado       :",self.estado)
        print("Horas de Contrato     :",self.horaContrato)
        self.horario.mostrarHorario()
