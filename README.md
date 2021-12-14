# Examen
Para el examen de programación hemos tendo que realizar dos tareas:

La primera, bajo eltítulo de "MINION GAME" deberíaa llevar a cabo las siguientes acciones:

Ambos jugadores reciben la misma cadena de caracteres
Ambos jugadores tienen que hacer subcadenas usando las letras de la cadena
Stuart tiene que formar palabras que comiencen con consonantes .
Kevin tiene que formar palabras que comiencen con vocales .
El juego termina cuando ambos jugadores han creado todas las subcadenas posibles.

Puntuación
Un jugador obtiene un +1punto por cada aparición de la subcadena en la cadena.

Mi código para este ejercicio sería el siguiente;


```print("Minion Game")
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
        print("Draw")
