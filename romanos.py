#creen un diccionari
simbolos = {"M":1000, "D":500, "C": 100, "L":50, "X":10, "V":5, "I":1}
tipo_5 = ("V", "D", "L")
tipo_1 = ("I", "X", "C", "M")
restas = ("CD", "CM", "XL", "XC", "IV", "IX")

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos: #upper es per forçar les mayusculas
            #isinstance, es per comprovar si una variable es d'un tipo especific, i sempre en dos paramentres
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido") #cadenas con formato
            #raise, es per obtindre una excepció
    else:
        raise ValueError(f"parametro {simbolo} debe ser un string")

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parametro {romano} debe ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = "" #valor anterior no vale nada primer i depues se acumula

    for letra in romano:
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError (f"Demasiado simbolos de tipo{letra}")
        if letra == valor_anterior:
            c_repes +=1
            if c_repes > 2:
                raise OverflowError (f"Demasiado simbolos de tipo{letra}")
            #overflowerror: massa quantitat desvordament
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior + letra not in restas:
                raise ValueError
            suma -= simbolos [valor_anterior] * 2 #suma i resta dos vegades per sumar al següent lletra, xq el valor del davant es més peque
            c_repes = 0
        else:
            c_repes = 0 #es per la lletra diferent i torne a contar a 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra
    return suma

