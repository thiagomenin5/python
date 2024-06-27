#Creando conjuntos con set()
conjunto = set(["thiago", "menin", "thiago"])
print(conjunto)

#metiendo un conjunto denro de otro conjunto
#frozenset: es un conjunto inmutable que no se puede modificar y se usa para meter conjuntos dentro de otros conjuntos
conjunto1= frozenset(["thiago", "menin"])
conjunto2 = {conjunto1, "menin4"}
