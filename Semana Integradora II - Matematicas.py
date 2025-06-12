from datetime import datetime

dni_1 = "37052504"
dni_2 = "42267088"
dni_3 = "42109622"

# Creacion de los conjuntos vacios
conjunto_1 = set()
conjunto_2 = set()
conjunto_3 = set()

# Agregando los DNI a los conjuntos
for i in range(0,8):
    conjunto_1.add(dni_1[i])
    conjunto_2.add(dni_2[i])
    conjunto_3.add(dni_3[i])

# Convirtiendo los elementos de los conjuntos de strings a enteros
conjunto_1 = {int(x) for x in conjunto_1}
conjunto_2 = {int(x) for x in conjunto_2}
conjunto_3 = {int(x) for x in conjunto_3}

# Mostrar los conjuntos por consola
print(f"Conjunto A = {conjunto_1}")
print(f"Conjunto B = {conjunto_2}")
print(f"Conjunto C = {conjunto_3}")

# Operaciones con los conjutos
union = conjunto_1.union(conjunto_2,conjunto_3)
interseccion = conjunto_1.intersection(conjunto_2,conjunto_3)
diferencia = conjunto_1.difference(conjunto_2,conjunto_3)
diferencia_simetrica = conjunto_1 ^ conjunto_2 ^ conjunto_3

# Mostrar las operaciones por consola
print(f"Unión: {union}")
print(f"Intersección:{interseccion}")
print(f"Diferencia:{diferencia}")
print(f"Diferencia simétrica:{diferencia_simetrica}")

# Contar Frecuencia de Cada DNI

def contar_frecuencia(dni):
    frecuencia = {}
    for digito in dni:
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

# Resultados
frecuencia_1 = contar_frecuencia(dni_1)
frecuencia_2 = contar_frecuencia(dni_2)
frecuencia_3 = contar_frecuencia(dni_3)

# Mostrar resultados
print("Frecuencia DNI 1:", frecuencia_1)
print("Frecuencia DNI 2:", frecuencia_2)
print("Frecuencia DNI 3:", frecuencia_3)


#Suma total de los dígitos de cada DNI.

sum_dni_1 = 0
sum_dni_2 = 0
sum_dni_3 = 0

# Recorremos cada DNI y hacemos la sumatoria.
for i in range(0,8):
    dni_1_int = int(dni_1[i])
    dni_2_int = int(dni_2[i])
    dni_3_int = int(dni_3[i])
    sum_dni_1 += dni_1_int
    sum_dni_2 += dni_2_int
    sum_dni_3 += dni_3_int

# Mostramos los resultados.
print(f"Suma de los elementos del conjunto A = {sum_dni_1}")
print(f"Suma de los elementos del conjunto B = {sum_dni_2}")
print(f"Suma de los elementos del conjunto C = {sum_dni_3}")

#Evaluacion de condiciones logica

if len(conjunto_1) > 6:
    print("Diversidad numérica alta")

if interseccion:
    print(f"{interseccion} Digitos compartidos")

#Operaciones con los anios de naciomiento

anios_nacimiento = [1995,1999,2000]

# Determinar si nacio en año par o impar
for i in range(0,3):
    if anios_nacimiento[i] % 2 == 0:
        print(f"Nació en {anios_nacimiento[i]} por lo tanto nació en año par")
    else:
        print(f"Nació en {anios_nacimiento[i]} por lo tanto nació en año impar")

# Determinar si todos los integrantes nacieron despues del 2000
if all(anio > 2000 for anio in anios_nacimiento):
    print("Grupo Z")

# Determinar si al menos uno de los integrantes nacio en un año bisiesto
for i in range(0,3):
    if (anios_nacimiento[i] % 4 == 0 and anios_nacimiento[i] % 100 != 0) or (anios_nacimiento[i] % 400) == 0:
        print(f'{anios_nacimiento[i]} Tenemos un año especial')

# Determinar si un año es bisiesto o no
def identificar_anio_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400) == 0:
        print(f'{anio} es un año bisiesto')
    else:
        print(f'{anio} no es un año bisiesto')

identificar_anio_bisiesto(1986) # Llamamos a la funcion y lo ponemos a prueba.

# Determinamos la edad aproximada de los integrantes usando solo su año de nacimiento.
def edad_aproximada(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento

edades = set() # Creamos un set vacio donde iran las edades.
# Agregamos las edades en el set.
for i in range(0,3):
    edades.add(edad_aproximada(anios_nacimiento[i]))

producto_cartesiano = {(año, edad) for año in anios_nacimiento for edad in edades} # Producto cartesiano entre las edades y los años de nacimiento.

# Mostramos el resultado.
print(f"Producto carteciano entre las edades: {producto_cartesiano}")

