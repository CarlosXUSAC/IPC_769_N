#include <stdio.h>
int main () {
    int grados, resultado;
    char operacion;
        
    printf("Seleccione Celsius(c) Fahrenheit(f): \n");

    operacion = getchar();

    switch(operacion){
        case 'c':
            grados = 0;
            resultado = 0;
            printf("\tCelsius\n");

            printf("Introduzca grados (C) salir: ");
                scanf("%d", &grados);
                resultado = grados * 1.8 + 32;                 

        break;

        case 'f':
            grados = 0;
            resultado = 1;
            printf("\tFahrenheit\n");

            printf("Introduzca grados (F) salir: ");
                scanf("%d", &grados);
                resultado = (grados - 32) / 1.8;

        break;     

        default:
            printf("Opcion invalida\n");                       

    }  
        
    
    printf("El resultado es: %d",resultado);
    return 0;
}