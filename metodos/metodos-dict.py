#Keys(): devuelve una lista con las claves del diccionario
diccionario = {"nombre": "Thiago", "edad": 22, "nacionalidad": "Argentina"}
resultado = diccionario.keys()
print(resultado)

#get(): devuelve el valor de la clave que le pasemos por parametro
resultado = diccionario.get("nombre")
print(resultado)

#clear(): elimina todos los items del diccionario
diccionario.clear()
print(diccionario)

#pop(): elimina el item que le pasemos por parametro y devuelve su valor
resultado = diccionario.pop("nombre")
print(resultado)
print(diccionario)

#items(): devuelve una lista de tuplas, cada tupla contiene la clave y el valor
resultado = diccionario.items()
print(resultado)

#copy(): devuelve una copia del diccionario
diccionario = {"nombre": "Thiago", "edad": 22, "nacionalidad": "Argentina"}
diccionario2 = diccionario.copy()
print(diccionario2)