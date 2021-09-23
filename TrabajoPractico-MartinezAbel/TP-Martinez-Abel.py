
class Empleado:
    def __init__(self, nombre, apellido, totalBasico, totalFull):
        self.nombre = nombre
        self.apellido = apellido
        self.totalBasico = totalBasico
        self.totalFull = totalFull

def verEmpleado():
        clear()
        print('Empleados: ')
        for empleado in listaEmpleados:
            print("nombre: {} - apellido: {} - total-full: {} - total-basico: {} ".format(empleado.nombre, empleado.apellido,  empleado.totalFull, empleado.totalBasico ) )


def verNombreEmpleado():
        print('Empleados: ')
        for empleado in listaEmpleados:
            print("nombre: {} ".format(empleado.nombre ) )

class Servicio:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Auto:
     def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


listaEmpleados = []
listaServicioBasico = []
listaServicioFull = []
listaAutoGrande = []
listaAutoChico = []


empleadoJ = Empleado("Jose", "Manzilla", 0, 0)
listaEmpleados.append(empleadoJ)
empleadoR = Empleado("Ramon", "Garcia", 0, 0)
listaEmpleados.append(empleadoR)
empleadoM = Empleado("Martin", "Lopez", 0, 0)
listaEmpleados.append(empleadoM)
empleadoL = Empleado("Luis", "Ramirez", 0, 0)
listaEmpleados.append(empleadoL)

servicioB = Servicio('Servicio basico', 250 , 0)
listaServicioBasico.append(servicioB)
servicioF = Servicio('Servicio full', 500, 0)
listaServicioFull.append(servicioF)

autoChico = Auto('Chico' , 0)
listaAutoChico.append(autoChico)
autoGrande = Auto('Grande' , 0)
listaAutoGrande.append(autoGrande)

def clear(): #funcion para limpiar terminal
    import os
    os.system ('cls')

def totalGeneral():
    clear()
    tg = 0
    tg = tg + (servicioB.cantidad * servicioB.precio) + (servicioF.cantidad * servicioF.precio)
    print(f'El total general es: {tg}')


def nuevoLavado():
    clear()
    print('--------------')
    print('INGRESANDO NUEVO LAVADO')
    print('**************')
    verNombreEmpleado()
    print('**************')
    option = input('Empleado a cargo del servicio: ').capitalize()
    print('-----------------------')
    if(option == 'Jose'):
        print('Tipo de lavado:')
        print('1- servicio Full')
        print('2- servicio Basico:')
        print('Seleccione una opcion para continuar')
        option = int(input(''))
        if(option == 1 ):
            servicioF.cantidad = servicioF.cantidad + 1
            empleadoJ.totalFull = empleadoJ.totalFull + servicioF.precio
            print('Tipo de Auto:')
            print('1- Grande:')
            print('2- Chico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            if(option == 1 ):
                autoChico.cantidad= autoChico.cantidad + 1
            elif(option == 2):
                autoGrande.cantidad= autoGrande.cantidad + 1

        elif(option == 2):
            servicioB.cantidad = servicioB.cantidad + 1
            empleadoJ.totalBasico = empleadoJ.totalBasico + servicioB.precio
            print('Tipo de Auto:')
            print('1- Grande:')
            print('2- Chico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            if(option == 1 ):
                autoChico.cantidad= autoChico.cantidad + 1
            elif(option == 2):
                autoGrande.cantidad= autoGrande.cantidad + 1
    elif(option == 'Ramon'):
        print('Tipo de lavado:')
        print('1- servicio Full')
        print('2- servicio Basico:')
        print('Seleccione una opcion para continuar')
        option = int(input(''))
        print('\n')
        if(option == 1 ):
            servicioF.cantidad = servicioF.cantidad + 1
            empleadoR.totalFull = empleadoR.totalFull + servicioF.precio
            print('Tipo de Auto:')
            print('1- Grande:')
            print('2- Chico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            if(option == 1 ):
                autoChico.cantidad= autoChico.cantidad + 1
            elif(option == 2):
                autoGrande.cantidad= autoGrande.cantidad + 1

        elif(option == 2):
            servicioB.cantidad = servicioB.cantidad + 1
            empleadoR.totalBasico = empleadoR.totalBasico + servicioB.precio
            print('Tipo de Auto:')
            print('1- Grande:')
            print('2- Chico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            if(option == 1 ):
                autoChico.cantidad= autoChico.cantidad + 1
            elif(option == 2):
                autoGrande.cantidad= autoGrande.cantidad + 1
    elif(option == 'Martin'):
            print('Tipo de lavado:')
            print('1- servicio Full')
            print('2- servicio Basico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            print('\n')
            if(option == 1 ):
                servicioF.cantidad = servicioF.cantidad + 1
                empleadoM.totalFull = empleadoM.totalFull + servicioF.precio
                print('Tipo de Auto:')
                print('1- Grande:')
                print('2- Chico:')
                print('Seleccione una opcion para continuar')
                option = int(input(''))
                if(option == 1 ):
                    autoChico.cantidad= autoChico.cantidad + 1
                elif(option == 2):
                    autoGrande.cantidad= autoGrande.cantidad + 1
            elif(option == 2):
                servicioB.cantidad = servicioB.cantidad + 1
                empleadoM.totalBasico = empleadoM.totalBasico + servicioB.precio
                print('Tipo de Auto:')
                print('1- Grande:')
                print('2- Chico:')
                print('Seleccione una opcion para continuar')
                option = int(input(''))
                if(option == 1 ):
                    autoChico.cantidad= autoChico.cantidad + 1
                elif(option == 2):
                    autoGrande.cantidad= autoGrande.cantidad + 1
    elif(option == 'Luis'):
            print('Tipo de lavado:')
            print('1- servicio Full')
            print('2- servicio Basico:')
            print('Seleccione una opcion para continuar')
            option = int(input(''))
            print('\n')
            if(option == 1 ):
                servicioF.cantidad = servicioF.cantidad + 1
                empleadoL.totalFull = empleadoL.totalFull + servicioF.precio
                print('Tipo de Auto:')
                print('1- Grande:')
                print('2- Chico:')
                print('Seleccione una opcion para continuar')
                option = int(input(''))
                if(option == 1 ):
                    autoChico.cantidad= autoChico.cantidad + 1
                elif(option == 2):
                    autoGrande.cantidad= autoGrande.cantidad + 1
            elif(option == 2):
                servicioB.cantidad = servicioB.cantidad + 1
                empleadoL.totalBasico = empleadoL.totalBasico + servicioB.precio
                print('Tipo de Auto:')
                print('1- Grande:')
                print('2- Chico:')
                print('Seleccione una opcion para continuar')
                option = int(input(''))
                if(option == 1 ):
                    autoChico.cantidad= autoChico.cantidad + 1
                elif(option == 2):
                    autoGrande.cantidad= autoGrande.cantidad + 1
    else:
        print('No se ha encontrado el empleado')

def menuVenta():
    clear()
    option = 0
    while(option != 4):
        print('-------------------------')
        print('MENU DE TOTAL')
        print('-------------------------')
        print('1- Total por empleado')
        print('2- Total por tipo de lavado')
        print('3- Total general')     
        print('4- Volver al menu principal')   
        option = int(input('Elija la operacion a realizar: '))
        print('\n')
        if(option == 1):
            verEmpleado()
        elif(option == 2):
            clear()
            print('-------------------------')
            print(f'Se relizaron {servicioB.cantidad} servicios Basicos')
            print(f'Se relizaron {servicioF.cantidad} servicios Full')
            print('-------------------------')
        elif(option == 3):
            totalGeneral()
        elif(option == 4):
            menuPrincipal()

def porcentaje(cantidades, total): #Funcion para calcular los porcentajes
      porcentaje = 100 * float(cantidades)/float(total)
      return porcentaje

def menuPorcentajes():
    clear() #menu de porcentajes
    op = 0
    while op != 3:
        print('-------------------------')
        print('MENU DE PROCENTAJES')
        print('-------------------------')
        print('1- Mostrar porcentaje de cada tipo de lavado')
        print('2- Mostrar porcentaje por tipo de auto (Chico o Grande)')
        print('3- Volver al menu principal')
        print('')
        op = int(input('Elija la operacion a realizar: '))
        print('')
        if op == 1:
            clear()
            totalLavados = servicioB.cantidad + servicioF.cantidad
            porcentajeBasico = porcentaje(servicioB.cantidad, totalLavados)
            porcentajeFull = porcentaje(servicioF.cantidad, totalLavados)
            print('')
            print('Se han realizo(aron):', totalLavados, 'lavado(s)')
            print('El porcentaje de', servicioB.nombre,'es de:', porcentajeBasico, '%')
            print('')  
            print('El porcentaje de', servicioF.nombre,'es de:', porcentajeFull, '%')
            print('')
        elif op == 2:
            clear()
            totalAutos = autoChico.cantidad + autoGrande.cantidad
            porcentajeChico = porcentaje(autoChico.cantidad, totalAutos)
            porcentajeGrande = porcentaje(autoGrande.cantidad, totalAutos)
            print('')
            print('Se han realizo(aron)', totalAutos, 'auto(s)')
            print('El porcentaje por tipo de auto', autoChico.nombre, 'es de:', porcentajeChico,'%')
            print('')
            print('El porcentaje por tipo de auto', autoGrande.nombre, 'es de:', porcentajeGrande,'%')
            print('')          

def menuPrincipal():
    clear()
    option = 0
    while( option != 4):
        print('**************')
        print('MENU PRINCIPAL')
        print('**************')
        print('1- Ingresar nuevo lavado')
        print('2- Menu ventas')
        print('3- Menu porcentajes')
        print('4- Salir')      
        option = int(input('Elija la operacion a realizar: '))
        if(option == 1):
            nuevoLavado()
        elif(option == 2):
            menuVenta()
        elif(option == 3):
            menuPorcentajes()
        elif(option == 4):
            clear()
            print('Programa Finalizado')
            exit()
        
menuPrincipal()
     

