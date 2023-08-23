#include <stdio.h>
int main () {
    int inicio, fin, factorial, resultado, cont = 0;
    float paso1, paso2, decimal;

    printf("Introduzca el inicio: ");
    scanf("%d", &inicio);
    printf("Introduzca el fin: ");
    scanf("%d", &fin);
    paso1 = inicio % 2;
    paso2 = fin % 2;    
    printf("%f\n", paso1);
    printf("%f\n", paso2);
    if(paso1 == 0 && paso2 == 0)
    {
        printf("Los numeros son pares\n");
        for(int i = inicio; i <= fin; i = i + 2)
        {
            printf("%d\n", i);
        }
    }
    else if(paso1 != 0 && paso2 != 0)
    {
        printf("Los numeros son impares\n");
        for(int i = inicio + 1; i <= fin; i = i + 2)
        {
            printf("%d\n", i);
            cont +=1;
        }
    }
    else
    {
        printf("Los numeros son mixtos\n");
        for(int i = inicio + 1; i <= fin + 1; i = i + 2)
        {
            printf("%d\n", i);
            cont +=1;
        }
    }
    printf("El total de numeros es: %d\n", cont);
    
}