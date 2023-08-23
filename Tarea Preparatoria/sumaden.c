#include <stdio.h>
int main () {
    int numero , resultado;
    char operacion , estado = 's';
        
    printf("Seleccione Suma(s) Multiplicacion(m): \n");

    operacion = getchar();

    switch(operacion){
        case 's':
            numero = 0;
            resultado = 0;
            printf("\tSumar\n");

            do{                
                printf("Introduzca numero (0) salir: ");
                scanf("%d", &numero);
                resultado += numero;                                                          
            }

            while(numero != 0);
        break;

        case 'm':
            numero = 0;
            resultado = 1;
            printf("\tMultiplicar\n");

            while(numero != 1){
                printf("Introduzca numero (1) salir: ");
                scanf("%d", &numero);
                resultado *= numero;
            }
        break;     

        default:
            printf("Opcion invalida\n");                       

    }  
        
    
    printf("El resultado es: %d",resultado);
    return 0;
}