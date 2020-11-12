#creen un diccionari
simbolos = {"M":1000, "D":500, "C": 100, "L":50, "X":10, "V":5, "I":1}

def romano_a_entero(romano):
    if isinstance(romano, str) and romano.upper() in simbolos: #upper es per forçar les mayusculas
        return simbolos[romano.upper()]
    elif isinstance(romano, str):
        raise ValueError(f"simbolo {romano} no permitido") #cadenas con formato
    else:
        raise ValueError(f"parametro {romano} debe ser un string")
