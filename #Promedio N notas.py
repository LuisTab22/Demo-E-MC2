#Promedio N notas
n = int(input("Ingrese cuantas notas va a promediar: "))
i = 1
suma = 0
while (i <= n):
    print("Ingrese las notas: ")
    nota = float(input())
    suma=suma+nota
    i+=1
prom = suma / n
print ("El promedio de notas es ", prom)