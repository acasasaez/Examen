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
print (tablero)