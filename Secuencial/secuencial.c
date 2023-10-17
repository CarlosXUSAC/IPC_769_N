#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int BusquedaSecuencial(int *parray, int buscar, int nelem);

void main(){
    int *pdatos, nelem, dbuscar, d, result;

    printf("Cuantos elementos desea en el array?");
    scanf("%d", &nelem);

    pdatos = (int*) malloc(nelem*sizeof(int));

    if(pdatos == NULL){
        printf("Insuficiente Espacio de Memoria");
        exit(-1);
    }

    for (d = 0; d < nelem; d++){
        printf("Elemento[%d]:", d);
        scanf("%d", (pdatos+d));
    }

    printf("\n Que elemento desea buscar?");
    scanf("%d", &dbuscar);

    result = BusquedaSecuencial(pdatos, dbuscar, nelem);

    if(result != -1)
        printf("\n%d Se encuentra en la posicion %d del array.\n", dbuscar, result);
    else
        printf("\n%d No se encontro en el array.\n", dbuscar);
    
}

int BusquedaSecuencial(int *parray, int buscar, int elem){
    int i;
    
    for(i = 0; i<elem; i++){
        if(*(parray+i) == buscar)
            return(i);
    }
    return(-1);
}