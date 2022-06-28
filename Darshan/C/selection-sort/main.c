#include<stdio.h>
#include "dependencies.h"


int main()
{
    int *list,n;

    printf("Enter the number of elements: ");
    scanf("%d",&n);

    MALLOC(list, sizeof(int)*n);

    printf("Enter the elements: ");

    for(int i=0;i<n;i++)
        scanf("%d",&list[i]);
    
    sort(list,n);

    printf("sorted list : ");
    for(int i=0;i<n-1;i++)
        printf("%d,",list[i]);
    printf("%d\n",list[n-1]);

    return 0;
}
