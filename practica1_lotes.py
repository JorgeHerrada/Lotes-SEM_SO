from linea import Linea

archivo = open("prueba2.txt", "r")

lineas = archivo.readlines()  # retorna LISTA de strings

archivo.close()

aux = Linea()

print("Lista de lineas inicial:")
print(lineas)


print("Lista de lineas sin salto final:")
lineas = aux.limpiarSaltos(lineas)
print(lineas)

salida = []
f = open('salida.txt', 'w')
f.close()

# itera por cada linea del texto
print("Comienza el ciclo")
for linea in lineas:

    print("elementos divididos:")
    elementos = aux.dividirLinea(linea)
    print(elementos, end="||")

    print("\nelementos sin basura:")
    elementos[0] = aux.limpiarBasura(elementos[0])
    print(elementos, end="||")

    print("\nDecimales:")
    decimales = elementos[0].split(":")
    for i in range(len(decimales)):
        decimales[i] = aux.hexaToDecimal(decimales[i])
    print(decimales)

    print("Hexadecimales:")
    hexadecimales = elementos[-1].split(".")
    for i in range(len(hexadecimales)):
        hexadecimales[i] = aux.decimalToHexa(hexadecimales[i])
    print(hexadecimales)

    # Unimos todo en el orden deseado
    print("Salida en orden:")
    salida.append(elementos[2] + "," + ":".join(decimales) +
                  "," + ".".join(hexadecimales) + "\n")
    print(salida)

    f = open('salida.txt', 'a')
    f.write(elementos[2] + "," + ":".join(decimales) +
            "," + ".".join(hexadecimales) + "\n")
    f.close()
