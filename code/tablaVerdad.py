from itertools import product

def generar_valores_verdad(n):
    combinaciones = list(product([True, False], repeat=n))
    valores_logicos = [[] for _ in range(n)]
    
    for combinacion in combinaciones:
        for i in range(n):
            valores_logicos[i].append(combinacion[i])
    
    return valores_logicos

def implica(A,B):
     pass

def tablaVerdad():
    print("Ingrese la sintaxis haciendo uso de paréntesis para la precedencia Ej. (A^B)→C:")
    variables = []
    funcion = input()

    for i in funcion:
        if (i.upper()).isalpha() and (not(i.upper() in variables)):
	        variables.append(i.upper())
    
    valores_logicos = generar_valores_verdad(len(variables))
    


tablaVerdad()

    

             

