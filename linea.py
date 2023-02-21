class Linea:

    # Recibe una lista de lineas, 
    # Retorna la lista de lineas sin los saltos de linea finales
    def limpiarSaltos(self,lineas):
        for i in range(len(lineas)):
            lineas[i] = lineas[i][:-1]
        
        return lineas

    # Recibe linea y retorna lista de elementos 
    # haciendo split por cada coma ","
    def dividirLinea(self,linea):
        return linea.split(",")

    
    def limpiarBasura(self,cadena):
        for i in range(len(cadena)-1,-1,-1):
            if cadena[i] == "/":
                return cadena[:i]
        
        return cadena


    def hexaToDecimal(self,hexa):
        return str(int(hexa,base=16))
    
    def decimalToHexa(self,decimal):
        return hex(int(decimal))[2:]
    
    
