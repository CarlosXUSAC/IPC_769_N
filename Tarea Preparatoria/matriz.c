#include <stdio.h>

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
    int arreglo[] = {3, 1, 2, 2, 3, 4, 4, 5, 6, 5};
    int tamano = sizeof(arreglo) / sizeof(arreglo[0]);

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
