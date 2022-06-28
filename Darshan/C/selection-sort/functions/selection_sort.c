#include "swap.h"
void sort(int *list, int n)
{
    for(int i=0;i<n-1;i++)
    {
        int min = i;
        for(int j=i+1;j<n;j++)
        {
            if(list[j]<list[min])
                min = j;
        }

        if(min != i)
           swap(&list[i],&list[min]); 
    }

    return;
}