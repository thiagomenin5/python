"""
Suponiendo que cada persona promedio habla dos palabaras por segundo...
A) Pedirle al usuario que diga cualquier texto real y calcular cuanto tardaria en decir esa frase y cuantas palabras fueron las que dijo.
B) Si tarda mas de 1 minuto, decirle "Para flaco, tampoco te pedi un testamento".
C) Cuanto tardaria dalto en decirlo, teniendo en cuenta que habla un 30% mas rapido.
"""
palabras_por_segundo = 2
frase = input("Ingresa cualquier frase que se te ocurra: ")

palabras_sueltas = frase.split(" ")
print(f"la frase contiene estas palabras: {palabras_sueltas}")

longitud_frase = len(palabras_sueltas)
print(f"tiene una cantidad de {longitud_frase} palabras la frase")

tiempo_hablado = longitud_frase / palabras_por_segundo



un_minuto_en_palabras = 120
if(tiempo_hablado < un_minuto_en_palabras):
    print(f"tardaste {tiempo_hablado} segundos en decir esa frase")
else:
    print("Para flaco, tampoco te pedi un testamento")
    
resta_habla_dalto = tiempo_hablado * 0.30
habla_dalto = tiempo_hablado - resta_habla_dalto
print(f"si lo diria dalto tardaria {habla_dalto} segundos en decirlo")