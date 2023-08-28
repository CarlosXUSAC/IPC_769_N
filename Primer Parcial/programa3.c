#include <stdio.h>

int main() {
    float precioQuetzales, precioSinIVA, montoIVA;

    printf("Ingrese el precio en quetzales: ");
    scanf("%f", &precioQuetzales);

    montoIVA = precioQuetzales * 0.12;

    precioSinIVA = precioQuetzales - montoIVA;

    printf("Precio sin IVA: %.2f quetzales\n", precioSinIVA);
    printf("Monto del IVA (12%%): %.2f quetzales\n", montoIVA);

    return 0;
}
