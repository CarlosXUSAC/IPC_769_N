#include <stdio.h>

int main () {
    int numero; 
    float resto;

    printf("Ingrese un numero entero: ");
    scanf("%d", &numero);  

    resto = numero % 2;
    
    if (resto == 0) {
        printf("El numero es par\n");
    }
    else {
        printf("El numero es impar\n");
    }

}