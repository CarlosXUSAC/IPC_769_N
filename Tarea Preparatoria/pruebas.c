#include <stdio.h>
#include <stdlib.h>

int main() {
    int arreglo[100]; 
    int indice = 0;
    char entrada[10]; 

    printf("Ingrese números enteros no negativos (deje en blanco para terminar):\n");

    while (1) {
        printf("Ingrese un número: ");
        fgets(entrada, sizeof(entrada), stdin);
    
        if (entrada[0] == '\n') {
            break;
        }

        int numero = atoi(entrada);

        if (numero < 0) {
            printf("Por favor, ingrese un número no negativo.\n");
        } else {
            arreglo[indice] = numero;
            indice++;

            if (indice >= sizeof(arreglo) / sizeof(arreglo[0])) {
                printf("El arreglo está lleno. Saliendo de la entrada de datos.\n");
                break;
            }
        }
    }

    printf("Elementos ingresados:\n");
    for (int i = 0; i < indice; i++) {
        printf("%d\n", arreglo[i]);
    }

    return 0;
}
