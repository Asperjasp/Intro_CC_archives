#include "stdio.h"
#include "stdbool.h"
int main()
{
    int Desde, Hasta;
    int opcion;
    bool continuar = true;
    while (continuar)
    {
        // Semejante a continuar == true
        // Programa para sumar los elementos pares en un rango [Desde, Hasta]
        printf("Programa para sumar los elementos pares en un rango [DESDE,HASTA]");
        printf("Inserte Desde: ");
        scanf("%d", &Desde);

        (Desde % 2) != 0 ? (Desde += 1) : (Desde); // el ? es una forma de if   ,

        printf("Inserte Hasta ");
        scanf("%d", &Hasta);
        int i = Desde;
        int suma = 0;
        while (i <= Hasta)
        {
            suma += i; // suma = suma +1
            i += 2;
        }
        // Es una variable acumulativa, se va a acumular un valor basado ene la nterior
        // Diferente de una variable contadora, por motivos.
        printf("El resultado es %d. \n ", suma);
        printf("Desea volver a ejectuar el programa  (1->Si/2->No) ");
        scanf("%d", &opcion);
        if (opcion == 2)
        {
            continuar = false;
        }
    }
    return 0;
}
