#include <stdio.h>

const float MI_A_KM = 1.609344;


float convMillasGalaKmLt(float millasPorGalon) {
    return millasPorGalon / 2.352;
}

int main() {
    float millasPorGalon;  

    printf("Ingrese la cantidad de millas por galon: ");
    scanf("%f", &millasPorGalon);
        
    float kilometrosPorLitro = convMillasGalaKmLt(millasPorGalon);
        
    printf("El equivalente en kilometros por litro es: %.2f\n", kilometrosPorLitro);
    
    return 0;
}
