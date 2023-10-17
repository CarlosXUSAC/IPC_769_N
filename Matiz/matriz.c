#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>


// Función para invertir el orden de un arreglo

void invertirOrden(int v[], int tam) {
    for (int i = 0; i < tam / 2; ++i) {
        int aux = v[i];
        v[i] = v[tam - 1 - i];
        v[tam - 1 - i] = aux;
    }
}

// Función para llenar la matriz con números aleatorios positivos

void llenarMatriz(int matriz[][50], int filas, int columnas) {
    for (int fila = 0; fila < filas; ++fila) {
        for (int col = 0; col < columnas; ++col) {
            matriz[fila][col] = rand() % 1000 + 1; // Números aleatorios entre 1 y 1000
        }
    }
}


int main() {
    const int filas = 2; // Dos filas
    const int columnas = 50; // 50 columnas
    
    int matriz[filas][columnas]; // Declarar una matriz de 2x50

    // Inicializar la semilla para los números aleatorios
    srand(time(NULL));

    // Llenar la matriz con números aleatorios positivos
    llenarMatriz(matriz, filas, columnas);

    // Mostrar la matriz original en la pantalla
    printf("Matriz original:\n");

    for (int fila = 0; fila < filas; ++fila) {
        for (int col = 0; col < columnas; ++col) {
            printf("%d ", matriz[fila][col]);
        }
        printf("\n"); // Cambiar de fila
    }   

    // Invertir el orden de la matriz
    for (int fila = 0; fila < filas; ++fila) {
        invertirOrden(matriz[fila], columnas);
    }

    // Mostrar la matriz invertida en la pantalla
    printf("\nMatriz invertida:\n");

    for (int fila = 0; fila < filas; ++fila) {
        for (int col = 0; col < columnas; ++col) {
            printf("%d ", matriz[fila][col]);
        }
        printf("\n"); // Cambiar de fila
    }

    return 0; // Terminar el programa con un código de salida 0 (éxito)
}