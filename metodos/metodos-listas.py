# LIST: crear una lista
lista = list(["holsa", "soy", "thiago"])

#LEN: Devuelve la longitud de la lista
cadena = "hola"
resultado = len(cadena)

#APPEND: Agrega un elemento al final de la lista
lista.append("y tu")
print(lista)

#EXTEND: Agrega los elementos de una lista al final de otra
lista.extend(["como", "estas"])
print(lista)

#INSERT: Inserta un elemento en la posicion que le indiquemos
lista.insert(1, "como")
print(lista)

#POP: Elimina el ultimo elemento de la lista o el que le indiquemos por parametro
lista.pop()
lista.pop(1)
print(lista)

#REMOVE: Elimina el primer elemento que coincida con el que le indiquemos
lista.remove("como")
print(lista)	

#CLEAR: Elimina todos los elementos de la lista
lista.clear()
print(lista)

#SORT: Ordena los elementos de la lista que sean numeros o booleanos
lista = [1, 4, 3, 2]
lista.sort()
print(lista)

#REVERSE: Invierte los elementos de la lista
lista.reverse()
print(lista)

