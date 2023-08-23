#include <stdio.h>
#include <stdlib.h>

int* eliminarDuplicados(int arr[], int *size) {

    if (*size <= 1) {
        return arr;
    }
    
    int aux[*size];
    int newSize = 0;  
    
    for (int i = 0; i < *size; i++) {
        int esDuplicado = 0;

        for (int j = 0; j < newSize; j++) {
            if (arr[i] == aux[j]) {
                esDuplicado = 1;
                break;
            }
        }

        if (!esDuplicado) {
            aux[newSize] = arr[i];
            newSize++;
        }
    }

    for (int i = 0; i < newSize; i++) {
        arr[i] = aux[i];
    }

    *size = newSize;

    return arr;
}

int main() {
    int arreglo[100];
    int tamano = sizeof(arreglo) / sizeof(arreglo[0]); ; 
    int indice = 0;
    char entrada[10];

     printf("Ingrese numeros enteros no negativos (deje en blanco para terminar):\n");

    while (1) {
        printf("Ingrese un numero: ");
        fgets(entrada, sizeof(entrada), stdin);
    
        if (entrada[0] == '\n') {
            break;
        }

        int numero = atoi(entrada);

        if (numero < 0) {
            printf("Por favor, ingrese un numero no negativo.\n");
        } else {
            arreglo[indice] = numero;
            indice++;

            if (indice >= sizeof(arreglo) / sizeof(arreglo[0])) {
                printf("El arreglo esta lleno. Saliendo de la entrada de datos.\n");
                break;
            }
        }
    }

    printf("Elementos ingresados:\n");
    for (int i = 0; i < indice; i++) {
        printf("%d\n", arreglo[i]);
    }

    printf("Arreglo original:\n");
    for (int i = 0; i < tamano; i++) {
        printf("%d ", arreglo[i]);
    }

    int *nuevoTamano = &tamano;
    int *resultado = eliminarDuplicados(arreglo, nuevoTamano);

    printf("\nArreglo sin duplicados:\n");
    for (int i = 0; i < *nuevoTamano; i++) {
        printf("%d ", resultado[i]);
    }

    return 0;
}
