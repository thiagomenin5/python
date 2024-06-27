cadena1 = "Hola soy thiago"
cadena2 = "bienvenido a mi blog"

#DIR -> Nos muestra los metodos que podemos utilizar con las cadenas
print(dir(cadena1))

# UPPER -> Convierte la cadena a mayusculas
print(cadena1.upper())

# LOWER -> Convierte la cadena a minusculas
print(cadena1.lower())

# TITLE -> Convierte la primera letra de cada palabra a mayuscula
print(cadena1.title())

# CAPITALIZE -> Convierte la primera letra de la cadena a mayuscula
print(cadena1.capitalize())

# FIND -> Busca una subcadena en la cadena y devuelve la posicion de la primera letra de la subcadena
print(cadena1.find("soy"))

# INDEX -> Busca una subcadena en la cadena y devuelve la posicion de la primera letra de la subcadena
print(cadena1.index("soy"))

# ISNUMERIC -> Devuelve True si la cadena es numerica
print(cadena1.isnumeric())

# ISALPHA -> Devuelve True si la cadena es alfabetica
print(cadena1.isalpha())

# COUNT -> Cuenta cuantas veces se repite una subcadena en la cadena
print(cadena1.count("a"))
# LEN -> Devuelve la longitud de la cadena
print(len(cadena1))

# ENDSWITH -> Devuelve True si la cadena termina con la subcadena que le pasamos
print(cadena1.endswith("thiago"))

# STARTSWITH -> Devuelve True si la cadena empieza con la subcadena que le pasamos
print(cadena1.startswith("Hola"))

# REPLACE -> Reemplaza una subcadena por otra
print(cadena1.replace("soy", "me llamo"))

# SPLIT -> Divide la cadena en una lista de subcadenas
print(cadena1.split(" "))

###################################################################################################################

# JOIN -> Une una lista de subcadenas en una sola cadena
print(" ".join(cadena1.split(" ")))

# STRIP -> Elimina los espacios en blanco al principio y al final de la cadena
print("    hola soy thiago    ".strip())

# LSTRIP -> Elimina los espacios en blanco al principio de la cadena
print("    hola soy thiago    ".lstrip())

# RSTRIP -> Elimina los espacios en blanco al final de la cadena
print("    hola soy thiago    ".rstrip())

# ISDIGIT -> Devuelve True si la cadena es un numero
print("123".isdigit())

# ISALNUM -> Devuelve True si la cadena es alfanumerica
print("123".isalnum())

# ISLOWER -> Devuelve True si la cadena esta en minusculas
print("hola".islower())

# ISUPPER -> Devuelve True si la cadena esta en mayusculas
print("HOLA".isupper())

# ISPRINTABLE -> Devuelve True si la cadena es imprimible
print("Hola soy thiago".isprintable())

# ISSPACE -> Devuelve True si la cadena es un espacio
print(" ".isspace())

# ISIDENTIFIER -> Devuelve True si la cadena es un identificador
print("hola".isidentifier())

# ISASCII -> Devuelve True si la cadena es ASCII
print("hola".isascii())

# ISDECIMAL -> Devuelve True si la cadena es un decimal
print("123".isdecimal())

# ISNUMERIC -> Devuelve True si la cadena es numerica
print("123".isnumeric())

# ISALPHA -> Devuelve True si la cadena es alfabetica
print("hola".isalpha())
