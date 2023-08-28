#include <stdio.h>

int main() {
    FILE *archivo;
    char escribir[] = "Esta es una cadena de ejemplo.\n";
    archivo = fopen("archivo.txt", "r+");

    if (archivo != NULL) {
        printf("El archivo se abrio correctamente.\n");
        fputs(escribir, archivo);
        fclose(archivo);
        }
    else {
        printf("Error al abrir el archivo.\n");
        printf("El archivo no existe.\n");
    }

    return 0;      
}