from itertools import product
from collections import deque

def generar_valores_verdad(n):
    combinaciones = list(product([True, False], repeat=n))
    valores_logicos = [[] for _ in range(n)]
    
    for combinacion in combinaciones:
        for i in range(n):
            valores_logicos[i].append(combinacion[i])
    
    return valores_logicos

def implica(A,B):
     pass

def obtenerPrecedencia(caracter):
     if(caracter == '~'):
          return 6
     elif(caracter == '∧'):
          return 5
     elif(caracter == '∨'):
          return 4
     elif(caracter == '⊕'):
          return 3
     elif(caracter == '→'):
          return 2
     elif(caracter == '↔'):
          return 1

def esOperador(caracter):
     caracteres ={'~', '∧','∨', '⊕', '→','↔'}
     if(caracter in caracteres):
          return True

def infijaPostfija(cadena):
    pila = deque()
    postfija = []

    for caracter in cadena:
        if caracter.isalnum():
            postfija.append(caracter.upper())
        elif(caracter == '('):
            pila.append(caracter)
        elif(caracter == ')'):
            while(pila and pila[-1] != '('):
                 postfija.append(pila.pop())
            pila.pop()
        elif(esOperador(caracter)):
            while(pila and obtenerPrecedencia(pila.top()) >= obtenerPrecedencia(caracter)):
                  postfija.append(pila.pop())
            pila.append(caracter)

    while(pila):
        postfija.append(pila.pop())

    return postfija

def evaluarPostfija(postfija):
    a = []
    b = []
    resultado = []
    pila = deque()

    for char in postfija:
        if not esOperador(char):
            pila.append(char)
        else:
             b = pila.pop()
             a = pila.pop()
             resultado = operacion(a,b,char)
             pila.append(resultado)

def operacion(a,b,caracter):
    if(caracter == '~'):
        pass
    elif(caracter == '∧'):
        return 5
    elif(caracter == '∨'):
        return 4
    elif(caracter == '⊕'):
        return 3
    elif(caracter == '→'):
        return 2
    elif(caracter == '↔'):
        return 1
    

def tablaVerdad():
    print("Ingrese la sintaxis haciendo uso de paréntesis para la precedencia Ej. (A^B)→C:")
    variables = []
    funcion = input()

    for i in funcion:
        if (i.upper()).isalpha() and (not(i.upper() in variables)):
	        variables.append(i.upper())
    
    valores_logicos = generar_valores_verdad(len(variables))

    postfija = infijaPostfija(funcion)
    nuevaPostfija = []
    for char in postfija:
        if not esOperador(char):
            index = variables.index(char)
            nuevaPostfija.append(valores_logicos[index])
        else:
             nuevaPostfija.append(char)



tablaVerdad()

    

             

