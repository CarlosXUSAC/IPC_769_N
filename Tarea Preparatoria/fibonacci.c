#include <stdio.h>

int main() {
    int n, i, t1 = 0, t2 = 1, siguiente;

    printf("Ingresa terminos de la serie: ");
    scanf("%d", &n);

    printf("Los %d terminos son:\n", n);

    // Mostrar los primeros n términos
    for (i = 1; i <= n + 1; ++i) {
        printf("%d, ", t1);
        siguiente = t1 + t2;
        t1 = t2;
        t2 = siguiente;
    }

    return 0;
}
