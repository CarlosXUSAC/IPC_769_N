
#include<stdio.h>
//#include<stdlib.h>

float pot (float n, int p);
int fac(int n);
int main (int argc, char *argv[])
{
	float x, seno=0;
	int n, cnt=1, cnt2=1;
	
	printf("\n Ingrese el angulo (grados): ");
	scanf("%f", &x);
    x=x*3.1416/180;
	printf("Elementos de la serie: ");
	scanf("%d", &n);
	
	for(cnt=1; cnt<=n; cnt++)
	{
		seno=seno+pot(-1,cnt+1)*pot(x,cnt2)/fac(cnt2);
		cnt2= cnt2+2;
	}
	printf("\n Seno (%0.2f)=%f",x, seno);
	return 0;
}

float pot(float b, int p)
{
	int k;
	float res=1;
	for(k=1; k<=p; k++)
	{
		res = res*b;
	}
	return(res);
}
int fac(int n)
{
	int k, f=1;
	for (k=1; k<=n; k++)
	{
		f=f*k;
	}
	return(f);
}

