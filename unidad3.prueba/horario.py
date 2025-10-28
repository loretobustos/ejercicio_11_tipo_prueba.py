class Horario():
    def __init__(self, jornada, horaInicio, horaTermino):
        self.jornada=jornada
        self.horaInicio=horaInicio
        self.horaTermino=horaTermino

    def mostrarHorario(self):
        print("Datos del Horario")
        print("Jornada           :",self.jornada)
        print("Hora de Inicio    :",self.horaInicio)
        print("Hora de Termino   :",self.horaTermino)
        

    def __str__(self) -> str:
        pass
    #tarea: toString