
Diccionario_planes={}
Diccionario_inscripciones={}

def validar_opcion():
        while True:
            try:
                opcion=int(input("Ingrese una opcion: "))
                if opcion!= 1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6:
                    print("La opcion ingresada en invalida, ingrese una opcion valida [1-2-3-4-5-6].")
                    menu()
                elif opcion<0:
                    print("La opcion ingresada no puede ser negativa.")
                    menu()
                else:
                    return opcion
            except Exception:
                print("Solo se permiten numeros en esta opcion.")
                menu()

def validacion_codigo():
    while True:
        codigo=input("Ingrese el codigo: ")
        if codigo in Diccionario_planes:
            print("El codigo ingresado ya existe.")
        else:
            return codigo
        
def buscar_codigo():
    codigo = input("Ingrese el código: ")

    if codigo in Diccionario_planes:
        return codigo
    else:
        print("El código no existe.")
        return None
    
def validar_nombre():
    while True:
        nombre=input("Ingrese el nombre: ")
        if nombre.strip()=="":
            print("El nombre no puede contener espacios vacios.")
        else:
            return nombre

def tipo_plan():
    while True:
        plan=input("Ingrese el tipo de plan [Anual-Semestral-Mensual]: ")
        if plan.lower().strip()=="anual":
            print("plan registrado correctamente.")
            return plan
        elif plan.lower().strip()=="semestral":
            print("plan registrado correctamente.") 
            return plan
        elif plan.lower().strip()=="mensual":
            print("Plan registrado correctamente.")
            return plan
        elif plan.isalpha!= True:
            print("Solo se permiten letras.")
        else:
            print("El plan ingresado es incorrecto ingrese una opcion valida [Anual-Semestral-Mensual].")
            continue

def duracion():
    while True:
        try:
            duracion=int(input("Ingrese la duracion del plan: "))
            if duracion<=0:
                print("El valor ingresado no puede ser 0 o menor.")
            else:
                return duracion
        except Exception:
            print("Solo se permiten numeros.")

def cupos_tipo(tipo):
    total_cupos = 0
    tipo_buscado = tipo_plan().lower().strip()
    for codigo, datos_inscripcion in Diccionario_inscripciones.items():
        tipo_plan_actual = datos_inscripcion[1].lower().strip()
        if tipo_plan_actual == tipo_buscado:
            if codigo in Diccionario_planes:
                cupos_disponibles = Diccionario_planes[codigo][1]
                total_cupos += cupos_disponibles
    print(f"\nEl total de cupos disponibles para el tipo de plan '{tipo}' es: {total_cupos}")


def acceso_piscina():
    while True:
        acceso=input("Ingrese si posee acceso a piscina [s/n]: ")
        if acceso.lower()!="s" and acceso.lower()!="n":
            print("Valor ingresado invalido, ingrese un valor valido [s/n].")
        elif len(acceso)>1:
            print("Solo puede ingresar un solo valor [s/n].")
        elif acceso.lower()=="s" or acceso.lower()=="n":
            return acceso
    
def incluye_clases():
    while True:
        clases=input("Ingrese si incluye clases [s/n]: ")
        if clases.lower()!="s" and clases.lower()!="n":
            print("El valor ingresado es invalido, ingrese un valor valido [s/n].")
        elif len(clases)>1:
            print("Solo puede ingresar un valor [s/n].") 
        else:
            return clases
        
def horario():
    while True:
        horario=input("Ingrese el horario [mañana-tarde-noche-libre]: ")
        if horario.strip()=="":
            print("No puede ingresar espacios vacios.")
        elif horario.lower().strip()=="noche":
            return horario
        elif horario.lower().strip()=="mañana":
            return horario
        elif horario.lower().strip()=="tarde":
            return horario
        elif horario.lower().strip()=="libre":
            return horario
        else:
            print("Tipo de horario ingresado invalido, ingrese una opcion valida.")


def precio():
    while True:
        try:
            precios=int(input("Ingrese el precio: "))
            if precios<=0:
                print("Valor ingresado incorrecto, ingrese un valor valido .")
            else:
                return precios 
        except Exception:
            print("Solo se permiten numeros.")

def Cupos():
    while True:
        try:
            cupo=int(input("Ingrese la cantidad de cupos disponibles: "))
            if cupo<0:
                print("El valor ingresado es menor a 0.")
            else:
                return cupo
        except Exception:
            print("Solo se permiten numeros.")

def agregar_plan(codigo, nombre, plan, durar, piscina,clases,
hora,precios,cupo):
    Diccionario_inscripciones[codigo]=[
        nombre,
        plan,
        durar,
        piscina,
        clases,
        hora
    ]

    Diccionario_planes[codigo]=[
        precios,
        cupo
    ]

def menu():

        while True:
            print("========== MENÚ PRINCIPAL ==========")
            print("[1] - Cupos por tipo de plan")
            print("[2] - Búsqueda de planes por rango de precio")
            print("[3] - Actualizar precio de plan")
            print("[4] - Agregar plan")
            print("[5] - Eliminar plan")
            print("[6] - Salir")
            print("=====================================")

            opcion=validar_opcion()

            if opcion ==1:
                cupo=cupos_tipo()
            elif opcion==3:
                codigo = buscar_codigo()
                if codigo is not None:
                    nuevo_precio = precio()
                    Diccionario_planes[codigo][0] = nuevo_precio
                    print("Precio actualizado correctamente.")

            elif opcion==4:

                    codigo=validacion_codigo()
                    nombre=validar_nombre()
                    plan=tipo_plan()
                    durar=duracion()
                    piscina=acceso_piscina()
                    clases=incluye_clases()
                    hora=horario()
                    precios=precio()
                    cupo=Cupos()
                    agregar_plan(codigo, nombre, plan, durar, piscina,clases,
                        hora,precios,cupo)
                    
            elif opcion==5:
                codigo = buscar_codigo()
                if codigo is not None:
                    del Diccionario_planes[codigo]
                    del Diccionario_inscripciones[codigo]
                    print("Plan eliminado correctamente.")

            elif opcion==6:
                print("Programa finalizado.")
                break

menu()