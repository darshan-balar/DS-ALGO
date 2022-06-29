#include "dependencies.h"

int main()
{
    int n;
    char *list;
    printf("Enter number of elements: ");
    scanf("%d",&n);

    MALLOC(list, sizeof(char)*(n+1));

    printf("Enter the elements: ");
    //for(int i=1;i<=n;i++)
        scanf("%s",list);

    perm(list,0,n);

    return 0;
}