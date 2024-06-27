#lista: se puede modificar el valor de los elementos, se puede agregar o eliminar elementos
lista = ["thiago menin", True, 3, 4.6]
#tupla: no se puede modificar el valor de los elementos, no se puede agregar o eliminar elementos
tupla = ("thiago menin", True, 3, 4.6)

#esto es valido
lista[3]= "modificado"

#esto no es valido
#tupla[3]= "modificado"

#creando un conjunto (set): no se puede modificar el valor de los elementos, no se puede agregar o eliminar elementos,pero se pueden redifinir los elementos
conjunto = {"thiago menin", True, 3, 4.6}

#creando un diccionario: 
diccionario = {
    "nombre": "thiago menin", 
    "es_estudiante": True, 
    "edad": 3, 
    "nota": 4.6
    }