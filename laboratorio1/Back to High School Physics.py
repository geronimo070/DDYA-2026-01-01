from sys import stdin

def main():
    datos = stdin.readline().split()
    for i in range(0,len(datos),2):
        velocidad = int(datos[i])
        tiempo = int(datos[i+1])
        tiempo_2 = tiempo*2
        resultado = tiempo_2* velocidad
        print( resultado)
        
main()
