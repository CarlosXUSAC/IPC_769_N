#include<stdio.h>
#include<stdlib.h>

void quicksort(int *izq, int *der);
void Intercambio(int *a, int *b);

void main(){
    int lista[] = {25, 8, 10, 4, 0, 3, 6};
    int i, nelem;
    nelem = sizeof(lista)/sizeof(int);
    printf("\n******ARRAY ORIGINAL******\n--------------------------\n");
    for(i=0; i< nelem; i++)
        printf("Element [%d]: %d \n", i+1, lista[i]);
    
    quicksort(&lista[0], &lista[nelem-1]);
    printf("\n \nARRAY ORDENADO EN FORMATO ASCENDENTE: \n");
    printf("--------------------\n");
    for (i = 0; i < nelem; i++)
    
        printf("Element [%d]: %d \n", i+1, lista[i]);
}

void quicksort(int *izq, int *der){
    if(der < izq)
        return;
    
    int pivot = *izq;
    int *ult = der;
    int *pri = izq;

    while (izq < der){
        while (*izq <= pivot && izq<(der+1))
            izq++;
        while (*der > pivot && der>(izq-1))
            der--;
        if(izq < der)
            Intercambio(izq, der);
    }
    Intercambio(pri, der);
    quicksort(pri, der-1);
    quicksort(der+1, ult);
}

void Intercambio(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}