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

def validacion_codigo()-> True |False:
    while True:
        codigo=input("Ingrese el codigo: ")
        if codigo in Diccionario_planes:
            return False
        else:
            return True
    
def validar_nombre():
    while True:
        nombre=input("Ingrese el nombre: ")
        if nombre.strip()=="":
            return False
        else:
            return True

def tipo_plan():
    while True:
        plan=input("Ingrese el tipo de plan [Anual-Semestral-Mensual]")
        if plan.lower()!="anual" and plan.lower()!="semestral" and plan.lower()!="mensual":
            return False
        elif plan.isalpha!= True:
            return False
        else:
            return True

def duracion():
    while True:
        try:
            duracion=int(input("Ingrese la duracion del plan: "))
            if duracion<=0:
                return False
            else:
                return True
        except Exception:
            return False

def acceso_piscina():
    while True:
        acceso=input("Ingrese si posee acceso a piscina [s/n]: ")
        if acceso.lower()!="s" and acceso.lower()!="n":
            return False
        elif len(acceso)>1:
            return False
        elif acceso.lower()=="s" or acceso.lower()=="n":
            return True
    

def incluye_clases():
    while True:
        clases=input("Ingrese si incluye clases [s/n]: ")
        if clases.lower()!="s" and clases.lower()!="n":
            return False
        elif len(clases)>1:
            return False 
        elif clases.lower=="s" or clases.lower()=="n":
            return True
        
def horario():
    while True:
        horario=input("Ingrese el horario: ")
        if horario.strip()=="":
            return False
        else:
            return True

def precio():
    while True:
        try:
            precios=int(input("Ingrese el precio: "))
            if precios<=0:
                return False
            else:
                return True
        except Exception:
            return False

def cupos():
    while True:
        try:
            cupo=int(input("Ingrese la cantidad de cupos disponibles: "))
            if cupo<0:
                print("Valor ingresado no puede ser menor a 0.")
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
                print(Diccionario_inscripciones)
                print(Diccionario_planes)
                

            if opcion==4:

                    codigo=validacion_codigo()
                    if codigo==False:
                        print("El codigo ingresado ya existe.")
                    else:
                        return codigo
                    
                    nombre=validar_nombre()
                    if nombre==False:
                        print("El nombre no puede ser un espacio en blanco, ingrese un nombre valido.")
                    else:
                        return nombre
                    
                    plan=tipo_plan()
                    if plan==False:
                        print("Ingrese una opcion valida por favor [Anual-Semestral-Mensual].")
                    else:
                        return plan

                    durar=duracion()
                    if durar==False:
                        print("el tiempo ingresado es invalido, por favor ingrese un valor valido.")
                    else:
                        return durar
                    
                    piscina=acceso_piscina()
                    if piscina==False:
                        print("La opcion ingresada es invalida, por favor ingrese una valida [s/n].")
                    else:
                        return piscina
                    
                    clases=incluye_clases()
                    if clases ==False:
                        print("Opcion ingresada invalida por favor ingrese una opcion valida [s/n].")
                    else:
                        return clases
                    
                    hora=horario()
                    if hora==False:
                        print("Opcion ingresada invalida, por favor ingrese una opcion vaida.")
                    else:
                        return True
                    
                    precios=precio()
                    if precios==False:
                        print("Valor ingresado invalido, por favor ingrese un valor valido.")
                    else:
                        return precios
                    
                    cupo=cupos()
                    if cupo==False:
                        print("Valor ingresado invalido, por favor ingrese un valor valido.")
                    else:
                        return cupo 

                    agregar_plan(codigo, nombre, plan, durar, piscina,clases,
        hora,precios,cupo)
                
            elif opcion==6:
                print("Programa finalizado.")
                break

menu()