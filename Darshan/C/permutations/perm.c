#include<stdio.h>

#define SWAP(x,y,z)  ((z = x),(x = y), (y=z))

void perm(char *list, int i,int n)
{
    char temp;
    if(i>=n)
    {
        for(int j=0;j<n-1;j++)
            printf("%c,",list[j]);
        printf("%c\n",list[n-1]);
    }
    else
    {
        for(int j=i;j<n;j++)
        {
            SWAP(list[i],list[j],temp);
            perm(list,i+1,n);
            SWAP(list[i],list[j],temp);
        }
    }
}