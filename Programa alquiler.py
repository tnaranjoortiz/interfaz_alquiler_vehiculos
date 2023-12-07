#%% EJERCICIO 1 y 2

import sys # Utilizaremos sys.exit() en el caso en que haya que finalizar el programa
           
# Creamos una lista para cada tabla del ejercicio, que contiene dentro diccionarios.

vehiculos = [
    {"Modelo": "Kia Picanto", "Categoría": "A", "Plazas": 5, "Mínimo": 1, "Coste": 8, "Descuento": 0.1, "Días min dcto": 4},
    {"Modelo": "Chevrolet Matiz", "Categoría": "A", "Plazas": 5, "Mínimo": 1, "Coste": 7},
    {"Modelo": "Citroën C1", "Categoría": "A", "Plazas": 4, "Mínimo": 3, "Coste": 5, "Descuento": 0.12, "Días min dcto": 5},
    {"Modelo": "Opel Corsa", "Categoría": "B", "Plazas": 4, "Mínimo": 2, "Coste": 8},
    {"Modelo": "Seat Ibiza", "Categoría": "B", "Plazas": 4, "Mínimo": 3, "Coste": 8},
    {"Modelo": "VW Caddy", "Categoría": "C", "Plazas": 7, "Mínimo": 6, "Coste": 9, "Descuento": 0.05, "Días min dcto": 3},
    {"Modelo": "Opel Zafira", "Categoría": "D", "Plazas": 9, "Mínimo": 5, "Coste": 12, "Descuento": 0.08, "Días min dcto": 4},
    {"Modelo": "Peugeot Expert", "Categoría": "D", "Plazas": 9, "Mínimo": 1, "Coste": 27},
    {"Modelo": "Hyundai Tucson", "Categoría": "D", "Plazas": 7, "Mínimo": 5, "Coste": 20},
    {"Modelo": "Mercedes Clase E", "Categoría": "E", "Plazas": 5, "Mínimo": 5, "Coste": 15, "Descuento": 0.1, "Días min dcto": 7},
    {"Modelo": "Jaguar XF", "Categoría": "E", "Plazas": 5, "Mínimo": 7, "Coste": 30},
    {"Modelo": "VW Polo", "Categoría": "B", "Plazas": 5, "Mínimo": 2, "Coste": 12, "Descuento": 0.05, "Días min dcto": 5}]

extras = [{"Extra": "Cancelación gratuita", "Coste": 2},
    {"Extra": "Cobertura de daños por colisión básica", "Coste": 15},
    {"Extra": "Cofre de equipaje en techo", "Coste": 20, "Categorías aplicables": ["B", "C", "D"]},
    {"Extra": "Ambientador de pino en retrovisor", "Coste": 30}]


# Creamos una función que calcule cómo queda el precio total para cada vehículo:
def precio_final(vehiculo, plazas, dias):
    coste_dia = vehiculo["Coste"]
    dcto = vehiculo.get("Descuento", 0)    # Usamos get para evitar un error en aquellos vehículos en que no aplica el descuento (y por tanto no hay key asociada)
    dias_dcto = vehiculo.get("Días min dcto", 0)
    
    if dias >= dias_dcto:
        coste = coste_dia * dias
        descuento = dcto * dias
        coste_total = coste - descuento
    else:
        coste_total = coste_dia * dias
        
    return coste_total


# Utilizamos bucles while para tratar de hacer el programa robusto ante comandos erróneos  (EJERCICIO 2 b))

while True:
    # Comenzamos preguntando al usuario por el período de alquiler
    d1 = int(input("\nIntroduzca el día en que desea recoger el vehículo (número del mes): "))
    d2 = int(input("\nIntroduzca el día de entrega (número del mes): "))
    
    # Calculamos el número de días de alquiler
    dias = d2 - d1 + 1    # Sumamos 1 para que incluya todo el rango temporal
    
    if dias <= 0 or dias >= 31:    # Verificamos que el tiempo de alquiler esté entre 1 y 31 días
        print("\nDebes introducir un período temporal válido, de un mes como máximo. Vuelva a intentarlo.\n")
    else:
        break


while True: 
    # Preguntamos ahora por el número de plazas
    plazas = int(input("\nIntroduzca el número de plazas que necesita: "))
    
    if plazas < 1:
        print("\nDebes introducir un número positivo de plazas. Vuelva a intentarlo.\n")
    elif plazas > 9:
        print("\nNo disponemos de vehículos de más de 9 plazas. Disculpe las molestias.\n")
    else:
       break


# Creamos una lista, donde iremos añadiendo diccionarios con los vehículos que encajan en esos requerimientos
opciones = []

for x in vehiculos:     # x señala a cada uno de los diccionarios de la lista
    if x["Plazas"] >= plazas and x["Mínimo"] <= dias:           
        precio_total = precio_final(x, plazas, dias)
        opciones.append({"Modelo": x["Modelo"], "Precio final": precio_total, "Categoría": x["Categoría"], "Plazas": x["Plazas"]})


# Indicamos al usuario los vehículos que puede alquilar.
if len(opciones) > 1:
    
    # Calculamos la opción más económica de la lista a través de la función min():
    economic = min(opciones, key=lambda x: x["Precio final"])     # Esto me crea un diccionario con la opción más barata
    x_economic = economic["Modelo"]    # Extraigo el nombre del vehículo más barato
    p_economic = economic["Precio final"]    # Extraigo el precio del vehículo más barato
    
    print("\n\nEn la siguiente lista le indicamos los vehículos disponibles y el cálculo del precio para el número de días indicados: ")
   
    for x in opciones:
        print("\n- " + x["Modelo"] + " (Categoría " + x["Categoría"] + ", " + str(x["Plazas"]) + " plazas). Precio final: " + str(x["Precio final"]) + "€")
    
    print("\nDe entre estas opciones, la más económica es", x_economic, "(" + str(p_economic) + "€).")
    
        
    while True:     # EJERCICIO 2 b)
        eleccion = input("\n\nIntroduzca el nombre del vehículo que desea elegir: ")  
        
        presente = False  # Creamos esta variable para testear si el nombre introducido se corresponde con uno de los vehículos en la lista opciones o no
        for x in opciones:
            if eleccion == x["Modelo"]:   
                presente = True
                break   # Si el nombre está en la lista, sale del bucle
            
        if presente:
            break
        else:   # Si el nombre no está en la lista, vuelve a preguntar por él
            print("\nEl nombre introducido no se corresponde con ninguno de los vehículos mencionados. Vuelva a intentarlo.")
        
        
elif len(opciones) == 1:
    print("\n\nEl único vehículo disponible, de acuerdo con sus necesidades, es el siguiente:")
    for x in opciones:
        print("\n- " + x["Modelo"] + " (Categoría " + x["Categoría"] + ", " + str(x["Plazas"]) + " plazas). Precio final: " + str(x["Precio final"]) + "€")
        
    a = (input("\n\nPara reservar dicho vehículo escriba OK: "))
    if a == "OK":
        eleccion = x["Modelo"]
    elif a != "OK": 
        print("\nSi lo desea, puede comenzar de nuevo la reserva para encontrar una mejor opción.")
        sys.exit()


print("\nDe acuerdo. Ha elegido", eleccion + ".")

for x in vehiculos:
    if x["Modelo"] == eleccion:
        categoria = x["Categoría"]    # Almacenamos esta variable para saber la categoría del coche elegido y usarla a continuación para los extras.


# Ofrecemos ahora los extras al usuario

if categoria in ["B", "C", "D"]:   # Verificamos que la elección pertenezca a alguna de estas categorías para ofrecer el extra 4
    print('''\n\n\nA continuación le mostramos los extras disponibles:
  1. Cancelación gratuita: 2€/día
  2. Cobertura de daños por colisión básica: 15€
  3. Ambientador de pino en retrovisor: 30€
  4. Cofre de equipaje en techo: 20€''')

else:
    print('''\n\n\nA continuación le mostramos los extras disponibles.
  1. Cancelación gratuita: 2€/día
  2. Cobertura de daños por colisión básica: 15€
  3. Ambientador de pino en retrovisor: 30€''')
          
extra = input("\nSi desea alguno de ellos, introduzca el número o números correspondientes, separados por comas: ")


eleccion_extras = []  # Creamos una lista para registrar los extras elegidos

if "1" in extra:
    eleccion_extras.append("Cancelación gratuita")
if "2" in extra:
    eleccion_extras.append("Cobertura de daños por colisión básica")
if "3" in extra:
    eleccion_extras.append("Ambientador de pino en retrovisor")
if "4" in extra:
    eleccion_extras.append("Cofre de equipaje en techo")


# EJERCICIO 2 a). Insistimos para que el usuario escoja el extra del ambientador.
if "3" not in extra:
    print("\n\nAntes de finalizar la reserva, ¿está seguro de que no desea adquirir el extra de 'Ambientador de pino en retrovisor'?")
    ambientador = input("\nEscriba 1 para incluirlo en su reserva, o intro para continuar sin hacerlo: ")
    
    if ambientador == str(1):
        eleccion_extras.append("Ambientador de pino en retrovisor")


# Calculamos el precio final

for x in opciones:
    if x["Modelo"] == eleccion:
        p = x["Precio final"]   # Tomamos el precio del vehículo elegido
        
        # Guardamos en variables también la categoría y plazas para luego usarlas en el recibo:
        categoria_recibo = x["Categoría"]
        plazas_recibo = x["Plazas"]
            
for x in extras:
    if x["Extra"] in eleccion_extras:
        p += x["Coste"]    # Sumamos el precio de los extras

if "Cancelación gratuita" in eleccion_extras:
    p += 2*(dias-1)  # Hacemos una condición adicional para incluir el precio de la cancelación gratuita, que no es un precio único sino un precio por día

# Calculamos el IVA y lo sumamos todo:
IVA = 0.21 * p
p_final_recibo = p + IVA


# Creamos el número de reserva aleatorio
import random
num_reserva = ''.join(random.choice('0123456789') for _ in range(8))


# Mostramos la información al usuario antes de proceder a la confirmación final
print("\n\nSegún el vehículo escogido y los extras, el precio total es de", str(round(p_final_recibo,2)) + "€.")
confirmacion_final = input("Si está conforme con el mismo, escriba OK para continuar con la reserva: ")

if confirmacion_final == "OK" or confirmacion_final == "ok":
    print("\n\nPara completar la reserva, introduzca sus datos a continuación.")
    nombre = input("Nombre y apellidos: ")
    dni = input("DNI: ")
    
    # Creamos un recibo con toda la información

    print("\n\nRESERVA REALIZADA")   
    print('-'*60)
    print(' ')
    print("Número de reserva:", num_reserva)
    print("\nNombre del titular:", nombre, "  DNI:", dni)             
    print("\nVehículo elegido:", eleccion + " (Categoría", categoria_recibo + ",", plazas_recibo, "plazas).")
    print("\nExtras elegidos:")
    for x in eleccion_extras:
        print("  -", x)
    print("\n\nPrecio final:", str(round(p_final_recibo,2)) + "€, IVA incluido.")

    print(' ')
    print('-'*60)

    print('''\n\nMuchas gracias por contratar nuestros servicios.
    \nPara cualquier consulta no dude en contactarnos.''')
    
    
    # EJERCICIO 2 c). Creación de un archivo con todas las reservas realizadas
    nombre_archivo = "registro.txt"
   
    # Usamos "a" para emplear el modo append, y se vayan incluyendo todas las reservas sin sobreescribirse
    with open(nombre_archivo, "a") as archivo:
        archivo.write("* RESERVA nº " + num_reserva) 
        archivo.write("\nNombre: " + nombre)
        archivo.write("\nDNI: " + dni)
        archivo.write("\nVehículo: " + eleccion)
        archivo.write("\nFechas: desde el día " + str(d1) + " hasta el día " + str(d2) + " (" + str(dias) + " días en total).")
        archivo.write("\nPrecio final (IVA incluido): " + str(round(p_final_recibo,2)) + "€")
        archivo.write("\n\n")

    
else:   # En el caso en que no se haya escrito OK para confirmar la reserva.
    print('''\n\nCancelamos la reserva actual.\nSi desea buscar otra opción diferente, puede volver a comenzar el proceso. \nPara cualquier consulta no dude en contactarnos. Muchas gracias.''')

