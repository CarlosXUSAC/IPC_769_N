#include <stdio.h>

int main() {
    char arreglo[50]; 
    int longitud = 50;   
    char nueva_arreglo[2 * longitud + 1];

    printf("Introduzca una arreglo: ");
    gets(arreglo);

    for (int i = 0; i < longitud; i++) {
        
        nueva_arreglo[2 * i] = arreglo[i];
        nueva_arreglo[2 * i + 1] = arreglo[i];
    }
        
    nueva_arreglo[2 * longitud] = '\0';
        
    printf("%s\n", nueva_arreglo);
    
    return 0;
}
