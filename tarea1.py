print("AJEDREZ EXTRAÑO")
import math
import random 
import sys
import re
import os
     
        
n =   random.randint(1, 100)
tablero =[[ " " for j in range (n)] for i in range (n)]
a = random.randint(0,n-1)
b = random.randint(0,n-1)
for i in range (n):
    for j in range (1):
        while not "j" in tablero [i]:
            if tablero [a][b] == " ":
                tablero[a][b] = "j"
                a = random.randint(0,n-1)
                b = random.randint(0,n-1)
            if tablero [a][b] == " ":
                tablero[a][b] = "j"
            a = random.randint(0,n-1)
            b = random.randint(0,n-1)
            if tablero [a][b] == " ":
             tablero[a][b] = "j"
for i in range (n):
    for j in range (1):
        while not "f" in tablero [i]:
            if tablero [a][b] == " ":
                tablero[a][b] = "f"
                a = random.randint(0,n-1)
                b = random.randint(0,n-1)
            if tablero [a][b] == " ":
                tablero[a][b] = "f"
            a = random.randint(0,n-1)
            b = random.randint(0,n-1)
            if tablero [a][b] == " ":
             tablero[a][b] = "f"
print ("El jugador que empieza toma la f")
print (tablero)