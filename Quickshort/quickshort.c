#include<stdio.h>
#include<stdlib.h>

void quicksort_ascendente(int [], int, int);
void quicksort_descendente(int [], int, int);

void main(){
    int lista[] = {25, 8, 10, 4, 0, 3, 6}, i, n_elementos;
    n_elementos = sizeof(lista)/sizeof(int);
    printf("\n******ARRAY ORIGINAL******\n--------------------------\n");
    for(i=0; i< n_elementos; i++)
        printf("%d ", lista[i]);
    
    quicksort_ascendente(lista, 0, n_elementos-1);
    printf("\n \nARRAY ORDENADO EN FORMATO ASCENDENTE: \n");
    printf("--------------------\n");
    for (i = 0; i < n_elementos; i++)
        printf("%d ", lista[i]);

    quicksort_descendente(lista, 0, n_elementos-1);
    printf("\n \nARRAY ORDENADO EN FORMATO DESCENDENTE: \n");
    printf("--------------------\n");
    for (i = 0; i < n_elementos; i++)
        printf("%d ", lista[i]);

    printf("\n \n");        
}

void quicksort_ascendente(int lista[], int inf, int sup){
    int mitad, x, izq, der;
    izq = inf;
    der = sup;
    mitad = lista[(izq+der)/2];

    do{
        while (lista[izq]<mitad && izq<sup)
            izq++;
        
        while (mitad<lista[der] && der>inf)
            der--;
        
        if(izq <= der){
            x = lista[izq];
            lista[izq] = lista[der];
            lista[der] = x;
            izq++;
            der--;
        }
    }while (izq <= der);

    if (inf<der)
        quicksort_ascendente(lista, inf, der);
    if (izq < sup)
        quicksort_ascendente(lista, izq, sup);
}

void quicksort_descendente(int lista[], int inf, int sup){
    int mitad, x, izq, der;
    izq = inf;
    der = sup;
    mitad = lista[(izq+der)/2];

    do{
        while (lista[izq]>mitad && izq<sup)
            izq++;
        
        while (mitad>lista[der] && der>inf)
            der--;
        
        if(izq <= der){
            x = lista[izq];
            lista[izq] = lista[der];
            lista[der] = x;
            izq++;
            der--;
        }
    }while (izq <= der);

    if (inf<der)
        quicksort_descendente(lista, inf, der);
    if (izq < sup)
        quicksort_descendente(lista, izq, sup);
}