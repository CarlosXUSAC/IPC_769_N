#include <stdio.h>
int main () {
    int n = 1, factorial = 1;    

    printf("Introduzca un numero: ");
    scanf("%d", &n);
    if (n == 0)
    {
        printf("0! = 1\n");
    }
    else if (n > 0)
    {
       for(int i = 1; i <= n; i += 1){
        factorial *= i;
        printf("%d! = %d\n", i, factorial);
       }
    }
    else
    {
        printf("Error!\n");  
        
    }
    
}