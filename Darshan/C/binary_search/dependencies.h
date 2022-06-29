#include<stdio.h>
#include<stdlib.h>
int binarysearch(int *,int,int);

#define MALLOC(p,s)\
        if(!((p)=malloc(s)))\
        {\
            printf("Insufficient memeory\n");\
            exit(EXIT_FAILURE);\
        }
