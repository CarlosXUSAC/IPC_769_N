#include <stdio.h>

int main(){
    char letra;

    printf("Introduce una letra\n");  
    scanf("%c", &letra);

    printf("El codigo ASCII de la letra %c es %i", letra, letra);

}