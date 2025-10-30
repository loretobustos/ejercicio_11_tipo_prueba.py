from sueldo import Sueldo
from horario import Horario

lista=[]

sue=Sueldo(1,"Rubilar","Adrian","Ing de Sistemas",45,True,
           Horario(1,"09:00","18:00"),1800000,500000,50000)
lista.append(sue)
sue=Sueldo(2,"Vargas","Juan","Ing de Sistemas",45,True,
           Horario(2,"12:00","21:00"),1600000,300000,0)
lista.append(sue)
sue=Sueldo(3,"Contreras","Sasha","Analista QA",45,True,
           Horario(3,"15:00","00:00"),2000000,200000,0)
lista.append(sue)
sue=Sueldo(4,"Barrera","Juan","Analista",45,False,
           Horario(1,"09:00","18:00"),900000,0,50000)
lista.append(sue)
sue=Sueldo(5,"Seguel","Tomás","Analista",45,True,
           Horario(2,"12:00","21:00"),1000000,100000,30000)
lista.append(sue)

#sue.listarCargos(lista)
listaJornada=sue.listarJornadaManana(lista)
print("Las persona de trabajan en la jornada de la mañana son:")
for item in listaJornada:
    print(item)



"""
Se pide:(¿Dónde se crea el método?)
    * listar todas las personas que cumplen el cargo de: xxxx (se lee por consola) se debe
      indicar si no hay personas que cumplan lo solicitado, por ejemplo: si se solicita
      listar a los "reponedores" y nadie cumple con este cargo, enviar mensaje 
    - listar todas las personas INACTIVAS
    - ¿Cuál es el promedio de rentas del personal (considerar sólo sueldo base)?
    * retornar una lista con todas las personas que trabajan en la mañana
    - retornar una lista con el horario de las personas 
    - ¿Quién gana "más" y quien gana "menos" en la empresa (considera sólo sueldo base)?
"""
    
