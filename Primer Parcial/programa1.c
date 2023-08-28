#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // números aleatorios
    srand(time(NULL));

    int sumaDados;
    int primerLanzamiento = 1; 

    while (1) {        
        int dado1 = rand() % 6 + 1;
        int dado2 = rand() % 6 + 1;

        sumaDados = dado1 + dado2;
        
        printf("Lanzamiento: %d + %d = %d\n", dado1, dado2, sumaDados);
        
        if (sumaDados == 8 && primerLanzamiento) {
            printf("Ganaste!\n");
            break;
        } else if (sumaDados == 7) {
            printf("Perdiste!\n");
            break;
        }
        
        primerLanzamiento = 0;
        
        char respuesta;
        printf("Quieres lanzar de nuevo? (s/n): ");
        scanf(" %c", &respuesta);

        if (respuesta != 's' && respuesta != 'S') {
            printf("Gracias por jugar. Hasta luego!\n");
            break;
        }
    }

    return 0;
}
