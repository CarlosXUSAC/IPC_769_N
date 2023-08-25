#include <stdio.h>

// Función para calcular el IMC dado el peso y la altura
float calcularIMC(float peso, float altura) {
    return peso / (altura * altura);
}

int main() {
    int opcion; // Variable para almacenar la opción del menú
    float peso, altura; // Variables para capturar el peso y la altura del usuario

    do {
        // Abrimos el archivo en modo de lectura ("r")
        FILE *archivo = fopen("historial.txt", "r");

        // Verificar si se pudo abrir el archivo correctamente
        if (archivo == NULL) {
            printf("No se pudo abrir el archivo para leer.\n");
            return 1; // Salir del programa con código de error
        }

        // Mostrar el menú al usuario
        printf("\n------------------\n");
        printf("Menu:\n");
        printf("1. Calcular IMC\n");
        printf("2. Ver historial\n");
        printf("3. Borrar historial\n");
        printf("4. Salida\n");
        printf("Elije una opcion: ");
        scanf("%d", &opcion); // Leer la opción elegida por el usuario

        switch (opcion) {
            case 1:
                // Capturar peso y altura del usuario
                printf("Ingrese el peso (kg): ");
                scanf("%f", &peso);
                printf("Ingrese la altura (m): ");
                scanf("%f", &altura);

                // Calcular el IMC usando la función calcularIMC
                float imc = calcularIMC(peso, altura);

                // Almacenar los datos en el archivo automáticamente
                FILE *archivo = fopen("historial.txt", "a"); // Abrir archivo en modo "append"
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo para escribir.\n");
                    return 1; // Salir del programa con código de error
                }
                fprintf(archivo, "Peso: %.2f kg, Altura: %.2f m, IMC: %.2f\n",
                        peso, altura, imc);
                fclose(archivo); // Cerrar archivo antes de salir

                printf("IMC calculado: %.2f\n", imc);

                if (imc<18.5){
                    printf("Su IMC es bajo");
                }else if (18.5<=imc<=24.9){
                    printf("Su IMC es normal");
                }else if (25<=imc<29.9){
                    printf("Su IMC es sobrepeso");
                }else if (imc>29.9){
                    printf("Su IMC es obeso");
                }
                
                break;

            case 2:
                // Mostrar el historial de IMC leyendo desde el archivo
                printf("Historial de IMC:\n");
                char linea[100]; // Variable para almacenar una línea del archivo
                while (fgets(linea, sizeof(linea), archivo) != NULL) {
                    printf("%s", linea); // Imprimir la línea leída
                }
                fclose(archivo); // Cerrar archivo después de leer

                break;

            case 3:
                // Borrar el contenido del archivo y cerrar el archivo antes de reabrir en modo "write"
                archivo = fopen("historial.txt", "w");
                if (archivo == NULL) {
                    printf("No se pudo abrir el archivo para escribir.\n");
                    return 1; // Salir del programa con código de error
                }
                fclose(archivo); // Cerrar archivo antes de salir
                printf("Historial borrado.\n");
                break;

            case 4:
                printf("Saliendo del programa.\n");
                break;

            default:
                printf("Opcion invalida. Por favor, elija una opcion valida.\n");
                break;
        }
    } while (opcion != 4); // Repetir el ciclo hasta que el usuario elija salir

    return 0; // Indicar que el programa finalizó correctamente
}
