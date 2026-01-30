from sys import stdin

def main():
    t= int(stdin.readline())    #ejercicio 11172 lab 01
    resultados = []
    for i in range (t):
        a, b= stdin.readline().split()
        a= int (a)
        b= int(b)
        if a > b:
            resultados.append(">")
        elif a < b:
            resultados.append("<")
        else:
            resultados.append("=")
    for n in resultados:
        print(n)
main()
