#include <stdio.h>

int esPrimo(int numero) {
    if (numero <= 1) {
        return 0;  
    }

    for (int i = 2; i * i <= numero; i++) {
        if (numero % i == 0) {
            return 0;  
        }
    }

    return 1;  
}

int main() {
    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    if (esPrimo(numero)) {
        printf("%d es un numero primo.\n", numero);
    } else {
        printf("%d es un numero compuesto.\n", numero);
    }

    return 0;
}
