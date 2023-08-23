#include <stdio.h>
#include <string.h>

int main () {
    int largo = 0;
    char arreglo[100];
    printf("Introduzca una arreglo: ");
    gets(arreglo);  
    largo = strlen(arreglo);
    printf("El largo de la arreglo es: %d", largo);
    return 0;
}