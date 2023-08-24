#include <stdio.h>
#include <math.h>

int main() {
    int opcion;
    double resultado;
    
    printf("Calculadora de Volumen\n");
    printf("1. Cubo\n");
    printf("2. Esfera\n");
    printf("3. Piramide de base triangular\n");
    printf("4. Piramide de base cuadrada\n");
    printf("Seleccione una opcion (1-4): ");
    scanf("%d", &opcion);

    switch (opcion) {
        case 1: // Cubo
            {
                double lado;
                printf("Ingrese la longitud del lado del cubo: ");
                scanf("%lf", &lado);
                resultado = pow(lado, 3);
                printf("El volumen del cubo es: %.2lf\n", resultado);
                break;
            }
        case 2: // Esfera
            {
                double radio;
                printf("Ingrese el radio de la esfera: ");
                scanf("%lf", &radio);
                resultado = (4.0 / 3.0) * M_PI * pow(radio, 3);
                printf("El volumen de la esfera es: %.2lf\n", resultado);
                break;
            }
        case 3: // Pirámide de base triangular
            {
                double base, altura;
                printf("Ingrese la longitud de la base de la piramide triangular: ");
                scanf("%lf", &base);
                printf("Ingrese la altura de la piramide triangular: ");
                scanf("%lf", &altura);
                resultado = (1.0 / 3.0) * (base * altura);
                printf("El volumen de la piramide de base triangular es: %.2lf\n", resultado);
                break;
            }
        case 4: // Pirámide de base cuadrada
            {
                double lado_base, altura;
                printf("Ingrese la longitud del lado de la base de la piramide cuadrada: ");
                scanf("%lf", &lado_base);
                printf("Ingrese la altura de la piramide cuadrada: ");
                scanf("%lf", &altura);
                resultado = (1.0 / 3.0) * pow(lado_base, 2) * altura;
                printf("El volumen de la piramide de base cuadrada es: %.2lf\n", resultado);
                break;
            }
        default:
            printf("Opcion no valida. Por favor, seleccione una opcion valida (1-4).\n");
    }

    return 0;
}
