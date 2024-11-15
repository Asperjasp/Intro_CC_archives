#include <stdio.h>
#include <stdlib.h>
void printArray(int *p, int len)
{
    for ()
}
int *dio(int *a, int *b, int lon)
{
    int arregloRetorno[lon];
    for (int i = 0; i < lon; i += 1)
    {
        arregloRetorno[i] = *(a + i) + *(b + i);
        // printf("%i\n", arregloRetorno[i]);
    }
    int *c;
    c = &arregloRetorno;
    return c;
}
int main()
{
    int billy[5] = {16, 2, 77, 40, 3};
    int anto[5] = {16, 2, 77, 40, 3};
    int longitud = sizeof(billy) / sizeof(billy[0]);

    int *a;
    a = dio(billy, anto, longitud);
    printArray(a, longitud)
        free(a);
    printArrar(a, longitud);
    for (int i = 0; i < longitud; i++)
    {
        printf("%i\n", *a);
        a++;
    }
    return 0;
}
