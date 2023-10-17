#include<stdio.h>
#include<stdlib.h>

void main(){
    float *pesos, indice;
    int i, j, nest, e;

    printf("Cuantos estudiantes son?: ");
    scanf("%d", &nest);

    pesos = (float *) malloc(nest *sizeof(float));

    if(pesos ==NULL){
        printf("Insuficiente espacio de memoria \n");
        exit(-1);
    }

    for(i=0; i<nest; i++){
        printf("Pesos del estudiante[%d]:", i+1);
        scanf("%f", &pesos[i]);
    }

    printf("\n***Array original***\n");
    for(i=0; i<nest; i++)
        printf("Pes[%d]: %.1f\n", i+1, pesos[i]);

    for (e=1; e<nest; e++){
        indice = pesos[e];
        j = e-1;
        while (j>=0 && pesos[j]>indice){
            pesos[j+1] = pesos[j];
            j--;
        }
        pesos[j+1] = indice;
    }

    printf("\n***Array Ordenado***\n");
    for(i=0; i<nest; i++)
        printf("Pes[%d]: %.1f\n", i+1, pesos[i]);

}