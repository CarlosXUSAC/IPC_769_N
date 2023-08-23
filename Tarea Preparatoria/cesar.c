#include <stdio.h>
#include <string.h>

int main () {
    char frase[100], fraseCifrada[100], intermedio[100];
    int largo, desplazamiento;
    
    printf("Ingrese una frase (Sin Mayusculas, Espacios o C. especiales): ");
    gets(frase);
    printf("Ingrese la cantidad de posiciones a desplazar: ");
    scanf("%d", &desplazamiento);

    largo = strlen(frase);   

    for (int i = 0; i < largo; i++)
    {
        intermedio[i] = ("%i", frase[i]);
        if (intermedio[i] > 122) {
            intermedio[i] = intermedio[i] - 26;}
        intermedio[i] = intermedio[i] + desplazamiento;        
    }

    for (int i = 0; i < largo; i++)
    {        
        fraseCifrada[i] = ("%c", intermedio[i]);                
    }
    
    printf("La frase cifrada es: ");
     for (int i = 0; i < largo; i++)
    {       
        printf("%c", fraseCifrada[i]);        
    }

}