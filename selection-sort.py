import random
import time
import matplotlib.pyplot as plt
import math

def selectionsort (liste): # Selection Sort
     for i in range(len(liste)):
         for j in range (i + 1, len(liste)):
             if liste[j] <= liste[i]:
                 liste[i], liste[j] = liste[j], liste[i]

def teste_sortiereung(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[j] <= liste[i]:
                return False
            else:
                return True


array = [1000, 2000, 4000, 8000, 16000, 32000]
sureler = list()
 # ... Eure Aufgabe ...

#n = int(input("n: "))
n = 1000
liste = [] # Leere Liste erzeugen
for i in range(n): # n Zahlen einfuegen
   liste.append(random.randint (0 ,1000)) # zufaellig in [0 ,10]

print(liste) # Ausgabe vor Sortieren
selectionsort (liste) # Sortieren
print(liste) # Ausgabe nach sortieren
print(teste_sortiereung(liste))

for n in array:
    liste = []  # Leere Liste erzeugen
    for i in range(n):  # n Zahlen einfuegen
        liste.append(random.randint(0, 1000))  # zufaellig in [0 ,10]
    t1 = time.perf_counter ()
    selectionsort(liste)
    t2 = time.perf_counter ()
    t=t2-t1
    sureler.append(t)
    print("Es sind",t ,"Sekunden vergangen", n)

for i in range(len(array)):
    array[i] = math.log10(array[i])
for i in range(len(sureler)):
    sureler[i] = math.log10(array[i])

plt.plot(array, sureler)
plt.show()