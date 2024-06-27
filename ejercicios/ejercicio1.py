"""
El timing para ver los conceptos vistos en python en un curso de corrido es de 2.5 horas como minimo, 7 horas como maximo y 4 horas de promedio. este curso lo logro en una hora y media.
A) Diferencia en porcentaje entre curso actual y:
    - el mas rapido de otros cursos
    - el mas lento de otros cursos
    - el promedio de otros cursos
B) Teniendo en cuenta que la cantidad de crudo en promedio de los demas cursos es de 5 horas y con edicion lo convierten en 4 horas y el crudo de este video fue de 3 horas y media y se redujo a una 
hora y media...
Que porcentaje de material inservible, se reduce del crudo en ambos casos?
   -el promedio de los cursos
-este curso
C) Ver 10 horas de otros cursos equivalente a cuantas horas de este curso? y al reves?
"""
curso_tiempo_minimo = 2.5
curso_tiempo_maximo = 7
curso_tiempo_promedio = 4
curso_tiempo_actual = 1.5

diferencia_curso_minimo = curso_tiempo_minimo - curso_tiempo_actual
porcentaje_diferencia_minimo = (diferencia_curso_minimo / curso_tiempo_actual) * 100
print(f"El curso mas rapido o de menor duracion es un  {porcentaje_diferencia_minimo}% mas lento que el actual")

diferencia_curso_promedio = curso_tiempo_promedio - curso_tiempo_actual
porcentaje_diferencia_promedio= (diferencia_curso_promedio / curso_tiempo_actual) *100
print(f"El curso promedio de duracion es un  {porcentaje_diferencia_promedio}% mas lento que el actual")

diferencia_curso_maximo = curso_tiempo_maximo - curso_tiempo_actual
porcentaje_diferencia_maximo=(diferencia_curso_maximo / curso_tiempo_actual) *100
print(f"El curso maximo de duracion es un  {porcentaje_diferencia_maximo}% mas lento que el actual")


crudo_promedio = 5
editado_promedio = 4
crudo_actual = 3.5
editado_actual=1.5

diferencia_crudo_promedio = crudo_promedio - editado_promedio
porcentaje_promedio_crudo= (diferencia_crudo_promedio / crudo_promedio) * 100
print(f"es un {porcentaje_promedio_crudo}% que va tirado a la basura del video promedio")

diferencia_crudo_actual = crudo_actual - editado_actual
porcentaje_actual_crudo=(diferencia_crudo_actual / crudo_actual) * 100
print(f"es un {porcentaje_actual_crudo}% que va tirado a la basura del video actual")