#include<stdio.h>

int i = 7;

int main()
{
    {
        int i = 8 ;
        printf("he");

        {
            int i = 9;
            {
                i = 5;
                printf("%d\n",i);
            }
        }
        printf("%d\n",i);

    }

}
