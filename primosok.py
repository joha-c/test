# # Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# # entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# # Resolucion:

#Un número primo es un número natural mayor que 1 que solo es divisible por 1 y por sí . no tiene divisores positivos distintos de 1 y de sí mismo. Por ejemplo, 2, 3, 5, 7 son primos. El 4 no es primo porque es divisible por 2. El 1 no se considera primo.
#Para determinar si un número es primo, se puede probar dividiéndolo por todos los números enteros desde 2 hasta la raíz cuadrada del número (o el número entero más cercano a la raíz cuadrada). Si no lo es, entonces es un número primo. 
#raiz_cuadrada = numero ** 0.5 El operador ** es el operador de exponenciación. Elevar un número a la potencia de 0.5 es lo mismo que calcular su raíz cuadrada. 
#Necesitamos una estructura de datos para ir añadiendo cada número que identifiquemos como primo. Para esto creamos una lista vacía [], ya que podemos agregar elementos dinámicamente. numeros_primos = []
#Tenemos que revisar cada número (numeroaprobar) (iterar)(for) dentro del rango 1 al 1000 (range(1,1001))
#Para cada numeroaprobar que examinamos, asumimos inicialmente que es primo(True) (SI ES 1 ES FALSO). Luego, intentaremos encontrar alguna razón por la cual no lo sea. Creamos una variable booleana llamada es_primo y la inicializamos en True para cada numeroaprobar al comienzo de la comprobación.
#¿Qué rango de posibles divisores debemos probar? Necesitamos probar si el númeroaprobar es divisible por algún otro número (divisoraprobar) dentro de un rango específico (1 al 1000). Sabemos que todos los números son divisibles por 1 y por sí mismos. Entonces, solo vamos a verificar si es divisible por algún número entre 2 y la raiz cuadrada de numeroaprobar + 1. Entonces, el rango a iterar para determinar el divisoraprobar va a quedar como range(2, numeroaprobar **0.5)
#for divisoraprobar in range(2, int(numeroaprobar**0.5) + 1): Este bucle interno itera a través de todos los posibles divisores desde 2 hasta el resultado de la raiz cuadrada entera de numeroaprobar actual mas 1. la convertimos a entero con int()
#¿Cómo sabemos si un numero es divisible por un divisor? Usamos el operador módulo (%). Si el resto de la división de numeroaprobar entre divisoraprobar es 0, significa que divisoraprobar divide a numeroaprobar exactamente, y por lo tanto, numeroaprobar no es primo (a menos que el divisor sea el propio número, pero ya excluimos esa posibilidad en nuestro rango de divisores).
#if numeroaprobar % divisoraprobar == 0:: Esta condición verifica si el resto de la división es 0.
#Si encontramos un divisor, el númeroaprobar no es primo entonces cambiamos el valor de nuestra variable es_primo a False y ya no hay necesidad de seguir probando con los demás posibles divisores.
#La instrucción break nos permite salir inmediatamente del bucle interno for divisoraprobar.
#Si el bucle interno for divisoraprobar se completa sin encontrar ningún divisor (o si el bucle nunca se ejecutó porque el numeroaprobar era 2), entonces la variable es_primo seguirá siendo True
#if es_primo: Esta condición verifica si el valor de es_primo sigue siendo True. Entonces si es primo, lo agregamos a la lista de numeros primos
#numeros_primos.append(numeroaprobar): El método append() añade el valor actual de numeroaprobar al final de la lista numeros_primos.
#print(numeros_primos): Esto mostrará en la consola todos los números que fueron añadidos a la lista.




numeros1al1000 = list(range(1, 1001))

numeros_primos = []

for numeroaprobar in numeros1al1000:
    if numeroaprobar > 1:  
        es_primo = True
        for divisoraprobar in range(2, int(numeroaprobar ** 0.5) + 1):
            if numeroaprobar % divisoraprobar == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numeroaprobar)

print(numeros_primos)