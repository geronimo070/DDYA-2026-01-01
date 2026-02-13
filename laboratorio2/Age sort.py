from sys import stdin
def main():
    n=int(stdin.readline())
    while n != 0:
        datos = stdin.readline().split()
        edades = []
        for i in range(n):
            edades.append(int(datos[i]))
        edades.sort()
        salida = ""
        for i in range(n):
            salida += str(edades[i])+""
        print(salida.strip())
        n = int(stdin.readline().strip())
    
        
        
main()
