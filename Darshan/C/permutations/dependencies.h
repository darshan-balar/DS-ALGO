void perm(char *, int,int);
#include <stdlib.h>
#include<stdio.h>
#define MALLOC(p,s) \
        if(!((p)=malloc(s))) \
        {\
            printf("Insufficient memory\n");\
            exit(EXIT_FAILURE);\
        }