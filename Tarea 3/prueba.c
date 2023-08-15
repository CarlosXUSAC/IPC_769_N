#include <stdio.h> //libreria para io
#include <stdlib.h> //li brería para ejecutar instrucciones del SO

int main() {
    double num1, num2;
    system("cls");
    printf("lngrese el primer numero: ");
    if (scanf("%lf", &num1) != 1) {
        printf("Error: Ingrese un numero real valido.\n");
        return 1;
    }

/* Aquí está el desglose de lo que está sucediendo:
scanf("%1f', &num1 ): Esta línea está utilízando la función scanf para leer un número real ingresado por el usuario y
asignarlo a la variable num1 .
El formato %1f se utilíza para leer números reales de doble precisión.
!= 1: Después de la llamada a scanf, se compara el valor devuelto por scanf con 1. scanf devuelve la cantidad de
elementos que se han leído con éxito.
En este caso, esperamos que se lea un solo elemento (un número real), por lo que comparamos con 1.
if ( ... ) { ... }: Esta estructura if verifica sí la condición entre paréntesis es verdadera.
Si el resultado de la comparación (scanf no leyó un solo elemento) es verdadero, se ejecutará el bloque de código de,
de las llaves { ... }.
}
printWError: Ingrese un número real válido.\n");: Si scanf no pudo leer un número real válido (es decir,
si el usuario ingresó algo que no es un número real), este bloque de código imprimirá un mensaje de error.
return 1 ;: Luego de imprimir el mensaje de error, el programa se detendrá y retornará el valor 1 al sistema operativo.
El valor 1 es comúnmente utilizado para indicar que el programa terminó con un error. */

    printf("lngrese el segundo numero: ");
    if (scanf("%lf", &num2) != 1) {    
        printf("Error: Ingrese un número real valido.\n");
        return 1;
    }

    double suma = num1 + num2;
    double resta = num1 - num2;
    double multiplicacion = num1 * num2;

    if (num2 == 0) {
        printf("Error: No se puede dividir entre cero.\n");
        return 1;
    }

    double division = num1 / num2;

    printf("\nResultados:\n" );
    printf("Suma: %.4lf\n", suma);
    printf("Resta: %.4lf\n", resta);
    printf("Multiplicacion: %.4lf\n", multiplicacion);
    printf("Division: %.4lf\n", division);
    return 0;
}