#include <stdio.h>

// Funciones para realizar las operaciones matemáticas
float suma(float a, float b) {
    return a + b;
}

float resta(float a, float b) {
    return a - b;
}

float multiplicacion(float a, float b) {
    return a * b;
}

float division(float a, float b) {
    if (b != 0) {
        return a / b;
    } else {
        printf("No se puede dividir por cero.\n");
        return 0;
    }
}

int main() {
    char nombre[100];
    FILE *historial;
    historial = fopen("historial.txt", "a");

    if (historial == NULL) {
        printf("Error al abrir el archivo de historial.\n");
        return 1;
    }

    int opcion;
    float resultado;
    float numero1, numero2;

    printf("Bienvenido al programa de operaciones matematicas.\n");
    printf("Por favor, ingrese su nombre: ");
    scanf("%s", nombre);

    do {
        printf("\nMenu de opciones:\n");
        printf("1. Suma\n");
        printf("2. Resta\n");
        printf("3. Multiplicacion\n");
        printf("4. Division\n");
        printf("5. Ver historial\n");
        printf("6. Borrar historial\n");
        printf("7. Salir\n");
        printf("Seleccione una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printf("Ingrese el primer numero: ");
                scanf("%f", &numero1);
                printf("Ingrese el segundo numero: ");
                scanf("%f", &numero2);
                resultado = suma(numero1, numero2);
                printf("El resultado de la suma es: %f\n", resultado);
                fprintf(historial, "%s - Suma - %.2f + %.2f = %.2f\n", nombre, numero1, numero2, resultado);
                break;
            case 2:
                printf("Ingrese el primer numero: ");
                scanf("%f", &numero1);
                printf("Ingrese el segundo numero: ");
                scanf("%f", &numero2);
                resultado = resta(numero1, numero2);
                printf("El resultado de la resta es: %f\n", resultado);
                fprintf(historial, "%s - Resta - %.2f - %.2f = %.2f\n", nombre, numero1, numero2, resultado);
                break;
            case 3:
                printf("Ingrese el primer numero: ");
                scanf("%f", &numero1);
                printf("Ingrese el segundo numero: ");
                scanf("%f", &numero2);
                resultado = multiplicacion(numero1, numero2);
                printf("El resultado de la multiplicacion es: %f\n", resultado);
                fprintf(historial, "%s - Multiplicacion - %.2f * %.2f = %.2f\n", nombre, numero1, numero2, resultado);
                break;
            case 4:
                printf("Ingrese el primer numero: ");
                scanf("%f", &numero1);
                printf("Ingrese el segundo numero: ");
                scanf("%f", &numero2);
                resultado = division(numero1, numero2);
                printf("El resultado de la division es: %f\n", resultado);
                fprintf(historial, "%s - Division - %.2f / %.2f = %.2f\n", nombre, numero1, numero2, resultado);
                break;
            case 5:
                fclose(historial);
                historial = fopen("historial.txt", "r");
                if (historial == NULL) {
                    printf("Error al abrir el archivo de historial.\n");
                    return 1;
                }
                char historial_line[200];
                printf("Historial de operaciones:\n");
                while (fgets(historial_line, sizeof(historial_line), historial) != NULL) {
                    printf("%s", historial_line);
                }
                fclose(historial);
                historial = fopen("historial.txt", "a");
                break;
            case 6:
                fclose(historial);
                historial = fopen("historial.txt", "w");
                if (historial == NULL) {
                    printf("Error al abrir el archivo de historial.\n");
                    return 1;
                }
                printf("Historial borrado.\n");
                fclose(historial);
                historial = fopen("historial.txt", "a");
                break;
            case 7:
                printf("Gracias por usar el programa. Hasta luego.\n");
                break;
            default:
                printf("Opcion no valida. Por favor, seleccione una opcion valida.\n");
        }
    } while (opcion != 7);

    fclose(historial);

    return 0;
}
