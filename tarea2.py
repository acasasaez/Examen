print("Minion Game")
palabra = input("introducir cadena de caracteres: ")
kevin = []
manolo=[]
def p():
    for i in palabra:
        
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            kevin.append(i)
    print("kevin",kevin)
    for i in palabra:
            if i != "a" and i != "e" and i!= "i" and i!= "o" and i!= "u":
                manolo.append(i)
    print ("manolo", manolo)
    print("puntos manolo", len(manolo))
    print("puntos kevin", len(kevin))
    if len(kevin) >len(manolo):
        print("Kevin ha ganado")
    if len(kevin) <len(manolo):
        print("Manolo ha ganado")
    if len(kevin) ==len(manolo):
        print("Empate")
    
p()