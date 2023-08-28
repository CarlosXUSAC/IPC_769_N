#include <stdio.h>
#include <string.h>

struct Estudiante {
    char nombre[50];
    char materias[5][50];
    float notas[5];
    float promedio;
};

int main() {
    FILE *archivo;
    struct Estudiante estudiante;
    int opcion;

    archivo = fopen("registro_notas.txt", "a+"); 

    if (archivo == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    while (1) {
        printf("\nMenu:\n");
        printf("1. Registrar nuevo estudiante y notas.\n");
        printf("2. Ver el historial de notas.\n");
        printf("3. Borrar el historial de notas.\n");
        printf("4. Salir.\n");
        printf("Seleccione una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printf("Nombre del estudiante: ");
                scanf("%s", estudiante.nombre);
                printf("Ingrese las materias y notas:\n");
                for (int i = 0; i < 5; i++) {
                    printf("Materia %d: ", i + 1);
                    scanf("%s", estudiante.materias[i]);
                    printf("Nota %d: ", i + 1);
                    scanf("%f", &estudiante.notas[i]);
                }
                estudiante.promedio = 0;
                for (int i = 0; i < 5; i++) {
                    estudiante.promedio += estudiante.notas[i];
                }
                estudiante.promedio /= 5;
                fwrite(&estudiante, sizeof(struct Estudiante), 1, archivo);
                printf("Estudiante y notas registrados exitosamente.\n");
                break;

            case 2:
                rewind(archivo); // Vuelve al principio del archivo
                printf("\nHistorial de notas:\n");
                while (fread(&estudiante, sizeof(struct Estudiante), 1, archivo)) {
                    printf("Nombre: %s\n", estudiante.nombre);
                    for (int i = 0; i < 5; i++) {
                        printf("Materia %d: %s, Nota: %.2f\n", i + 1, estudiante.materias[i], estudiante.notas[i]);
                    }
                    printf("Promedio: %.2f\n", estudiante.promedio);
                }
                break;

            case 3:
                fclose(archivo);
                archivo = fopen("registro_notas.txt", "w"); // Abre el archivo en modo escritura (borra el contenido)
                printf("Historial de notas borrado.\n");
                break;

            case 4:
                fclose(archivo);
                return 0;

            default:
                printf("Opción no válida.\n");
        }
    }

    return 0;
}
