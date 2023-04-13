# determinar la frecuencia de cada palabra de un archivo txt
f = open('hola.txt', 'r')
m = open('frecuencia.txt', 'w')
frecuencia = {}
for linea in f:
    if linea in frecuencia:
        frecuencia[linea] += 1
    else:
        frecuencia[linea] = 1

for linea, cantidad in frecuencia.items():
    m.write(str(cantidad) + '\n')