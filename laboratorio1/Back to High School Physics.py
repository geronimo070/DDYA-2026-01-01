from sys import stdin

def main():
    for linea in stdin:
        datos = linea.split()
        velocidad = int(datos[0])
        tiempo = int(datos[1])
        tiempo_2 = tiempo*2
        resultado = tiempo_2* velocidad
        print( resultado)
        
main()
