#include <stdio.h>
#include <math.h>

int main() {
    float calificaciones[5];
    float suma = 0.0, media, varianza = 0.0, desviacion_estandar;
    int i, j, contador, max_contador = 0;
    float moda, rango;
    
    // Pedir al usuario ingresar las calificaciones
    printf("Ingrese 5 calificaciones (de 0 a 100):\n");
    
    for (i = 0; i < 5; i++) {
        scanf("%f", &calificaciones[i]);
        suma += calificaciones[i];
    }
    
    // Calcular la media
    media = suma / 5.0;
    
    // Calcular la varianza
    for (i = 0; i < 5; i++) {
        varianza += pow(calificaciones[i] - media, 2);
    }
    varianza /= 5.0;
    
    // Calcular la desviación estándar
    desviacion_estandar = sqrt(varianza);
    
    // Calcular la moda
    for (i = 0; i < 5; i++) {
        contador = 0;
        for (j = 0; j < 5; j++) {
            if (calificaciones[j] == calificaciones[i]) {
                contador++;
            }
        }
        if (contador > max_contador) {
            max_contador = contador;
            moda = calificaciones[i];
        }
    }
    
    // Calcular el rango
    float max = calificaciones[0];
    float min = calificaciones[0];
    
    for (i = 1; i < 5; i++) {
        if (calificaciones[i] > max) {
            max = calificaciones[i];
        }
        if (calificaciones[i] < min) {
            min = calificaciones[i];
        }
    }
    rango = max - min;
    
    // Mostrar los resultados
    printf("Media: %.2f\n", media);
    printf("Mediana: %.2f\n", calificaciones[2]); // Dado que solo se ingresaron 5 calificaciones, la mediana es el valor del medio.
    printf("Moda: %.2f\n", moda);
    printf("Rango: %.2f\n", rango);
    printf("Desviacion Estandar: %.2f\n", desviacion_estandar);
    printf("Varianza: %.2f\n", varianza);
    
    return 0;
}
