# Constante de Kaprekar en Python

### Descripción del teorema
El número **6174** es conocido como la **Constante de Kaprekar**. Este número es el resultado de la aplicación repetida de la **Operación de Kaprekar** que consiste en los siguientes pasos:

1.  Escoger cualquier número de cuatro dígitos. La única restricción es que no pueden ser los 4 dígitos iguales. 
2. Ordenar los cuatro dígitos en orden descendente, para obtener el mínimo valor con esos dígitos. 
3.  Ordenar los mismos cuatro dígitos en orden ascendente, para obtener el máximo valor con esos dígitos. 
4.  Calcular el resto, restando el máximo valor con el mínimo valor. 
5.  Si el resto no es igual a **6174**, repetir los cuatro pasos anteriores, añadiendo ceros siempre que sea necesario para completar los cuatro dígitos. 

Por ejemplo, supongamos que partimos del número de cuatro dígitos 5342:

    5432 – 2345 = 3087

    8730 – 0378 = 8352

    8532 – 2358 = 6174

### Para ejecutar
Clonar el repositorio: 

    git clone https://github.com/marcoscerioni/Kaprekar.git
 Abrimos la carpeta en donde está el archivo .py. 
     
     cd Kaprekar
 Ejecutamos el archivo kaprekar. py
     
     python3 kaprekar.py


