#creen un diccionari simbolos
simbolos = {"M":1000, "D":500, "C": 100, "L":50, "X":10, "V":5, "I":1}
tipo_5 = ("V", "D", "L")
restas = ("CD", "CM", "XL", "XC", "IV", "IX")

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos: #upper es per forçar les mayusculas
    #isinstance, es per comprovar si una variable es d'un tipo específic, i sempre en dos paramentres
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido") #cadenas con formato
            #raise, es per obtindre una excepció
    else:
        raise ValueError(f"parametro {simbolo} debe ser un string")

def orden_magnitud(caracter):
    valor = simbolo_a_entero(caracter)
    return len(str(valor))
   
def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parametro {romano} debe ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = "" #valor anterior no val res: primer i depueés s'acumula
    orden_magnitud_global = 0
    orden_magnitud_letra = 0
    ha_habido_resta = False

    for letra in romano:
            orden_magnitud_letra = orden_magnitud(letra)
            if letra == valor_anterior:
                orden_magnitud_global = orden_magnitud_letra
                if letra in tipo_5:
                    raise ValueError("No és romano")
                elif c_repes >= 2:
                    raise ValueError("Massa repeticions")
                elif ha_habido_resta:
                    raise ValueError("Massa restes")
                c_repes += 1
            elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
                if valor_anterior + letra not in restas:
                    raise ValueError("Resta no permessa")
                elif c_repes > 0:
                    raise ValueError("Resta tras repetició no permesa")
                elif ha_habido_resta:
                    raise ValueError("Massa restes")

                ha_habido_resta = True
                suma -= 2*simbolo_a_entero(valor_anterior)
                #suma i resta dos vegades per sumar al següent lletra, xq el valor del davant es més peque
                c_repes = 0
            else:
                if orden_magnitud_global > orden_magnitud_letra:
                    ha_habido_resta = False

                if ha_habido_resta:
                    raise ValueError("Massa restes")

                orden_magnitud_global = orden_magnitud_letra
                c_repes = 0 #es per la lletra diferent i torne a contar a 0

            suma = suma + simbolo_a_entero(letra)
            valor_anterior = letra    
    return suma



    #overflowerror: massa quantitat desvordament         

"""
estaopcié es aplicant potàcines i divisions
def descomponer(numero):

    l = []
    for pot in (1000, 100,10): #son les 3 podentcies xq no cal les unitats 1987. EL POT ES POTENCIA
        l.append(numero // pot) # [1,9,8]
        numero = numero % pot  # 87%10=7

    l.append(numero)
    return l

"""

def descomponer(numero):
    l = []
    for d in str(numero):  #d es igual a cada digito
        l.append(int(d))
    return l

    #return [int(d) for d in str(numero)] es lo mateix que la part de dalt però simplificat
    # es una compressió de listas 

lista_millares =("M",)
lista_centenas = ("C", "D", "M")
lista_decenas = ("X", "L", "C")
lista_unidades = ("I", "V", "X")

lista_ordenes = [lista_unidades, lista_decenas, lista_centenas, lista_millares]


def convertir(ordenes_magnitud):  # 1.9.8.7
    contador = 0
    resultado = []
    for orden in ordenes_magnitud[::-1]: # estos simbolos entre corchetes es per recorrer la llista del rebes
        resultado.append(procesar_simbolos (orden, lista_ordenes[contador]))
        contador += 1

    return "".join(reversed(resultado)) #join es una funcion de las cadenas el contenido de la lista i intercala


def procesar_simbolos(s, clave):
    if s == 9:
        return clave[0] + clave[2]
    elif s >= 5:
        return clave[1] + clave[0]*(s-5)
    elif s == 4:
        return clave[0] + clave[1]
    else:
        return clave[0]*s


def entero_a_romano(numero):
    if not isinstance(numero, int):
        raise SyntaxError(f"{numero} no és número natural")

    if numero < 1 or numero > 3999:
        raise OverflowError(f"{numero} ha de estar entre 1 i 3999")

    ordenes_magnitud = descomponer(numero)
    romano = convertir(ordenes_magnitud)
    return romano