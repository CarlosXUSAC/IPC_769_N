#include <stdio.h>
int main () {
    int n;
    printf("Introduzca un numero: ");
    scanf("%d", &n);
    for(int i = 1; i <= 10; i += 1)
    {
        printf("%d x %d = %d\n", n, i, (n * i));
    }
    
}