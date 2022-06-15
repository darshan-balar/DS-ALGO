// it is a good practice to intialize pointers when declared
// if no address is available at the time of declaration then assign null value

#include<stdio.h>

int main()
{
    int *null_pointer = NULL;

    printf("the value of pointer is : %p\n",null_pointer);

    return 0;
}