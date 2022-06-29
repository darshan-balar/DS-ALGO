#include "dependencies.h"
int main()
{
    int n,*list,key;

    printf("Enter the number of elements: ");
    scanf("%d",&n);

    MALLOC(list, sizeof(int)*n);

    printf("Enter %d elements in sorted order: ",n);
    for(int i=0;i<n;i++)
        scanf("%d",&list[i]);
    
    printf("Enter the element to be searched: ");
    scanf("%d",&key);
    
    int index = binarysearch(list,n,key);

    if(index == -1)
        printf("Not present\n");
    else
        printf("element present at position %d\n",index+1);
    
    return 0;
}