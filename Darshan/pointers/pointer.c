// pointers are like variables, but instead of storing actual values 
// they store address of some other location
// using that address we can access the data present at that location


#include<stdio.h>

int main()
{
    int i = 5;
    int *pointer;  //declaration which says the type of data it will be pointing to

    pointer = &i;  

    printf("The value of i : %d\n",i);
    printf("The value of pointer : %p\n",pointer);
    printf("The value at pointer : %d\n",*pointer);

    return 0;


}