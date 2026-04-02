nombre = input("Ingrese nombre del cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese nombre del cliente: ")

cant_input = input("¿Cuántos productos va a comprar?: ")
while not cant_input.isdigit() or int(cant_input) == 0:
    print("Error: Ingrese un número entero mayor a cero.")
    cant_input = input("¿Cuántos productos va a comprar?: ")

cantidad = int(cant_input)
total_sin_desc = 0
total_con_desc = 0

for i in range(1, cantidad + 1):
    
    precio_input = input(f"Producto {i} - Precio: ")
    while not precio_input.isdigit():
        print("Error: Ingrese un precio válido (solo números).")
        precio_input = input(f"Producto {i} - Precio: ")
    
    precio = int(precio_input)
    total_sin_desc += precio

    tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_desc not in ['s', 'n']:
        print("Error: Ingrese 'S' para sí o 'N' para no.")
        tiene_desc = input("¿Tiene descuento? (S/N): ").lower()

    if tiene_desc == 's':
        precio_final = precio * 0.90 
    else:
        precio_final = precio
    
    total_con_desc += precio_final

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

        #EJERCICIO 2  — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta= "python123 "
intentos= 3
usuario= input("ingrese su usuario: ")
clave=input("ingrese su clave: ")
intentos -=1

while not(usuario == usuario_correcto and clave== clave_correcta)and intentos>0:
    print("error, ingrese nuevamente: ")
    print(f"intentos restantes {intentos}")
    intentos -=1
    usuario= input("Ingrese su usuario: ")
    clave=input("Ingrese su clave: ")
if usuario== usuario_correcto and clave== clave_correcta:
    print(f"felicidades, ingresaste con intentos restantes{intentos}")
    opcion=""
    while opcion!="4":
        print("1. Ver estado de inscripción (mostrar “Inscripto”)")
        print("2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir") 
        print("3. Mostrar mensaje motivacional (1 frase)") 
        print("4. Salir") 
        opcion= input("elija una opcion: ")
        if not opcion.isdigit():
            print("ERROR, ELIJA UN NUMERO VALIDO")
            continue
        if int(opcion)< 1 or int(opcion)> 4:
            print("opcion fuera de rango")
            continue
        if opcion== "1":
            print("Inscripto")
        elif opcion == "2":
            clave_nueva=input("Ingrese su nueva clave (6 digitos, puede contener letras): ")
            if len(clave_nueva)<6:
                print("Clave muy corta")
            else:
                confirma=input("Confirme su clave: ")
                if clave_nueva==confirma:
                    print("Clave confirmada")
                else:
                    print("error, no coinciden las claves")
        elif opcion == "3":
            print("¡Tu puedes con todo!")
    print("cuenta finalizada")
else:
    print(f"cuenta bloqueada intentos: {intentos}")




                # EJERCICIO 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” 
dia = ""
lunes1=""
lunes2=""
lunes3=""
lunes4=""

martes1=""
martes2=""
martes3=""
operador= input("Ingrese su nombre: ")
while not operador.isalpha():
     print("error solo se permiten letras")
     operador= input("Ingrese su nombre: ")
opciones=""        
while opciones!="5":
    print("1. Reservar turno") 
    print("2. Cancelar turno (por nombre)") 
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opciones=input("Seleccione una opció(1-5)")
    if not opciones.isdigit():
        print("Ingrese un numero valido")
        continue
    opcion_num=int(opciones)
    if int(opcion_num)< 1 or int(opcion_num)> 5:
            print("opcion fuera de rango")
            continue
    if opcion_num == 1:
         print("Reservar")
         print("1. lunes")
         print("2. martes")  
         dia_elegido= input("Dia elegido: ")
         if dia_elegido=="1":
            paciente=input("Ingrese el nombre del paciente: ")
            while not paciente.isalpha():
                 print("incorrecto, solo letras")
                 paciente=input("Ingrese el nombre del paciente: ")
            if lunes1=="":
                    lunes1 = paciente
                    print(f"turno 1 (Lunes) reservado para {paciente}")
            elif lunes2 == "":
                      lunes2 = paciente
                      print(f"turno 2 (Lunes) reservado para {paciente}")
            elif lunes3=="":
                      lunes3 = paciente
                      print(f"turno 3 (Lunes) reservado para {paciente}")
            elif lunes4=="":
                      lunes4= paciente
                      print(f"turno 4 (Lunes) reservado para {paciente}")
            else:
                   print("Agenda completa")
         elif dia_elegido=="2":
            paciente=input("Ingrese el nombre del paciente: ")
            while not paciente.isalpha():
                 print("Incorrecto, solo letras")
                 paciente= input("ingrese el nombre del paciente: ")
            if martes1 =="":
                      martes1 =  paciente
                      print(f"Turno 1 (Martes) reservado para {paciente}. ")
            elif martes2 =="":
                      martes2 = paciente
                      print(f"Turno 2 (Martes) reservado para {paciente}. ")
            elif martes3 == "":
                      martes3= paciente
                      print(f"Turno 3 (Martes) reservado para {paciente}. ")
            else:
                   print("Agenda completa")
    elif opcion_num==2:
           print("cancelar turno")
           print("1. Dia lunes")
           print("2. Dia martes")
           dia_c=input("Elija el dia que quiere cancelar: ")
           if dia_c == "1":
             paciente_c=input("Nombre del paciente a cancelar: ")
             if paciente_c == lunes1:
                    lunes1 =""
                    print(f"Se cancelo el turno de {paciente_c}")
        
             elif paciente_c == lunes2:
                    lunes2=""
                    print(f"Se cancelo el turno de {paciente_c}")
             elif paciente_c== lunes3:
                    lunes3=""
                    print(f"Se cancelo el turno de {paciente_c}")
             elif paciente_c== lunes4:
                    lunes4=""
                    print(f"Se cancelo el turno de {paciente_c}")
             else:
                    print("No se encontró pacientes reservados ese dia")
           elif dia_c =="2":
                paciente_c=input("Nombre del paciente a cancelar:")
                if paciente_c== martes1:
                       martes1=""
                       print(f"Se cancelo el turno de {paciente_c}")
                elif paciente_c == martes2:
                       martes2=""
                       print(f"Se cancelo el turno de {paciente_c}")
                elif paciente_c== martes3:
                       martes3=""
                       print(f"Se cancelo el turno de {paciente_c}")
                else:
                       print("No se encontró pacientes reservados ese dia")
    elif opcion_num==3:
           print("VER AGENDA DEL DIA")
           print("1. lunes")
           print("2. Martes")
           dia_v=input("¿Que dia quiere ver?: ")
           if dia_v== "1":
                  print(f"Agenda del lunes {operador}")
                  if lunes1=="":
                         print("Turno 1 libre")
                  else:
                         print(f"Turno 1 : {lunes1}")
                  if lunes2=="":
                        print("Turno 2 libre") 
                  else:
                         print(f"Turno 2 : {lunes2}")
                  if lunes3=="":
                         print("Turno 3 libre")
                  else:
                         print(f"Turno 3 : {lunes3}")
                  if lunes4 =="":
                         print("Turno 4 libre")
                  else:
                         print(f"Turno 4 : {lunes4}")
           elif dia_v== "2":
                   if martes1=="":
                          print("Turno 1 libre")
                   else:
                          print(f"Turno 1 : {martes1}")   
                   if martes2=="":
                          print("Turno 2 libre")
                   else:
                          print(f"Turno 2 : {martes2}") 
                   if martes3=="":
                          print("Turno 3 libre")
                   else:
                          print(f"Turno 3 : {martes3}") 
    elif opcion_num==4:
           print("Ver resumen general")
           ocupados_lunes=0
           if lunes1 != "":
                  ocupados_lunes+= 1
           if lunes2 !="":
                   ocupados_lunes+= 1
           if lunes3!= "":
                  ocupados_lunes+=1
           if lunes4!="":
                ocupados_lunes+=1

           ocupados_martes=0
           if martes1 !="":
                  ocupados_martes+=1
           if martes2!="":                  
                ocupados_martes+=1
           if martes3!="":
                ocupados_martes+=1       
                
           libre_lunes=4 - ocupados_lunes
           libres_martes=3 - ocupados_martes
           print(f"Lunes: {ocupados_lunes} ocupados y {libre_lunes} libres.")
           print(f"Martes: {ocupados_martes} ocupados y {libres_martes} libres.")                              
            
           if ocupados_lunes> ocupados_martes:
                  print("El dia con mayor turnos es el Lunes")
           elif ocupados_martes > ocupados_lunes:
                  print("El dia con mayor turnos es el martes")
           else:
                  print("Ambos dias tienen la misma cantidad de turnos agendados")
    elif opcion_num == 5:
        print("RESUMEN FINAL DE LA JORNADA")
        print("Operador:", operador)
        
       
        print("Pacientes atendidos el Lunes:")
        if lunes1 != "":
            print("Turno 1:", lunes1)
        if lunes2 != "":
            print("Turno 2:", lunes2)
        if lunes3 != "":
            print("Turno 3:", lunes3)
        if lunes4 != "":
            print("Turno 4:", lunes4)
        
        
        if lunes1 == "" and lunes2 == "" and lunes3 == "" and lunes4 == "":
            print("No hubo pacientes registrados.")

        
        print("Pacientes atendidos el Martes:")
        if martes1 != "":
            print("Turno 1:", martes1)
        if martes2 != "":
            print("Turno 2:", martes2)
        if martes3 != "":
            print("Turno 3:", martes3)
            
        if martes1 == "" and martes2 == "" and martes3 == "":
            print("No hubo pacientes registrados.")

                #EJERCICIO 4  — “Escape Room: La Bóveda”
                # Variables iniciales (fijas)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0 
nombre = input("Ingrese nombre del agente: ")
while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese nombre del agente: ")

print("Agente identificado:", nombre)

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == True:
        if tiempo <= 3:
            print("SISTEMA BLOQUEADO. Se perdió el acceso a la bóveda.")
            energia = 0
            continue 

    print("--- ESTADO ---")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    
    if alarma == True:
        print("ALERTA: Alarma activada")
    else:
        print("Estado: Silencioso")

    print("1. Forzar cerradura (-20 energia, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3 tiempo)")
    print("3. Descansar (+15 energia, -1 tiempo)")
    
    opcion = input("Elija accion (1-3): ")
    
    while not opcion.isdigit():
        print("Error: ingrese un numero.")
        opcion = input("Elija accion (1-3): ")
    
    if opcion == "1":
        racha_forzar = racha_forzar + 1
        energia = energia - 20
        tiempo = tiempo - 2
        
        if racha_forzar == 3:
            print("¡La cerradura se trabo! Alarma activada.")
            alarma = True
        else:
            if energia < 40:
                print("Riesgo de alarma. Elija un numero del 1 al 3:")
                n_alarma = input("Numero: ")
                while not n_alarma.isdigit():
                    n_alarma = input("Numero (1-3): ")
                
                if n_alarma == "3":
                    alarma = True
                    print("¡Alarma activada!")
            if alarma == False:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("¡Cerradura abierta!")
    elif opcion == "2":
        racha_forzar = 0 
        energia = energia - 10
        tiempo = tiempo - 3
        print("Iniciando hackeo...")
        for i in range(1, 5):
            print("Paso", i, "completado.")
            codigo_parcial = codigo_parcial + "A"
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("¡Hackeo exitoso! Cerradura abierta.")
                codigo_parcial = ""
    elif opcion == "3":
        racha_forzar = 0 
        tiempo = tiempo - 1
        if alarma == True:
            print("Dificultad para descansar por la alarma (-10 extra)")
            energia = energia - 10
        energia = energia + 15
        if energia > 100:
            energia = 100
        print("Energia recuperada.")
if cerraduras_abiertas == 3:
    print("VICTORIA. Has abierto la boveda, agente", nombre)
else:
    if energia <= 0:
        print("DERROTA. Te quedaste sin energia.")
    elif tiempo <= 0:
        print("DERROTA. Se acabo el tiempo.")


#Ejercicio 5  — “Escape Room:"La Arena del Gladiador"  
import random
nombre_gladiador=input("Ingrese el nombre del gladiador: ")

while nombre_gladiador=="" or not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador=input("Ingrese el nombre del gladiador: ")

nombre_gladiador=nombre_gladiador.capitalize()

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3 
danio_base_gladiador = 15 
danio_base_enemigo = 12
turno_gladiador=True

while vida_gladiador>0 and vida_enemigo>0:
    if turno_gladiador:
        print(f"La vida de {nombre_gladiador} es {vida_gladiador}")
        print(f"La vida del enemigo es {vida_enemigo}")
        print(f"Cantidad de pociones de cura disponibles {pociones_vida}")
        while True:
            opcion=input('''
                Indique la accion a realizar:
                1)Ataque pesado
                2)Ataque por rafaga
                3)Curar
                ''')
            while opcion=="" or not opcion.isdigit():
                print("Error: Solo se permiten numeros")
                opcion=input('''
                Indique la accion a realizar:
                1)Ataque pesado
                2)Ataque por rafaga
                3)Curar
                ''')
            opcion=int(opcion)
            match opcion:
                case 1:
                    if vida_enemigo<20:
                        vida_enemigo=vida_enemigo-1.5*danio_base_gladiador
                        print(f"Atacaste al enemigo por {1.5*danio_base_gladiador} puntos de daño")
                    else:
                        vida_enemigo=vida_enemigo-danio_base_gladiador
                        print(f"Atacaste al enemigo por {danio_base_gladiador} puntos de daño")
                    turno_gladiador=False
                    break
                case 2:
                    rafaga=random.randint(1,4)
                    for _ in range(rafaga):
                        vida_enemigo-=5
                        print("> Golpe conectado por 5 de daño")
                    turno_gladiador=False
                    break
                case 3:
                    if pociones_vida>0:
                        vida_gladiador=vida_gladiador+30
                        pociones_vida-=1
                        print(f"Te curaste, tu vida sube a {vida_gladiador}")
                        print(f"Las pociones de cura quedan en {pociones_vida} pociones restantes.")
                    else:
                        print("No dispone de mas pociones de vida")
                        print("Pierdes el turno")
                    turno_gladiador=False
                    break
                case _:
                    print("La opcion ingresada no es valida")
                    print("Intente de nuevo")
    else:
        print("Turno de ataque del enemigo!!")
        vida_gladiador=vida_gladiador-danio_base_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador=True

if vida_gladiador>0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print(f"DERROTA. Has caído en combate.")
