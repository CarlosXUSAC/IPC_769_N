#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int BusquedaBinaria(int datos[], int nelem, int clave);

void OrdenarBurbuja(int datos[], int nelem){
    int i, j, temp;
    for(i=0; i<nelem; i++)
        for(j=0; j<(nelem-1); j++)
            if(datos[j]> datos[j+1]){
                temp = datos[j];
                datos[j] = datos[j+1];
                datos[j+1] = temp;
            }
}

void main(){
    int *pdatos, nelem, dbuscar, d, result;

    printf("Cuantos elementos desea en el array?");
    scanf("%d", &nelem);
    pdatos = (int*) malloc(nelem*sizeof(int));

    if(pdatos==NULL){
        printf("Insuficiente espacio de memoria");
        exit(-1);
    }

    for (d = 0; d < nelem; d++){
        printf("Elemento[%d]:", d);
        scanf("%d", (pdatos+d));
    }

    OrdenarBurbuja(pdatos, nelem);

    printf("\n Que elemento desea buscar?");
    scanf("%d", &dbuscar);

    result = BusquedaBinaria(pdatos, nelem, dbuscar);

    if(result!=-1)
        printf("\n %d Se encuentra en la posicion %d del array.", dbuscar, result);
    else
        printf("\n%d no se enecontro en el array.\n", dbuscar);

}

int BusquedaBinaria(int lista[], int n, int clave){
    int central, bajo, alto; 
    int valorCentral;
    bajo = 0;
    alto = n-1;

    while (bajo <= alto){
        central = (bajo+alto)/2;
        valorCentral = lista[central];

        if(clave == valorCentral)
            return(central);
        else if (clave < valorCentral)
            alto = central-1;
        else
            bajo = central+1;   
    }

    return(-1);
    
}