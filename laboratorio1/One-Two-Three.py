from sys import stdin
def main():
    n = int(stdin.readline())
    for i in range (n):
        palabra = stdin.readline().strip()
        if len(palabra)== 5:
            print(3)
        else:
            similitud = 0
            if palabra [0] == "o":
                similitud += 1
            if palabra [1] == "n":
                similitud += 1
            if palabra [2] == "e":
                similitud += 1
            if similitud >= 2:
                print(1)
            else:
                print(2)     
main()
