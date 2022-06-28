void sort(int *, int);
#include <stdlib.h>
#define MALLOC(p,s) \
        if(!((p)=malloc(s))) \
        {\
            printf("Insufficient memory\n");\
            exit(EXIT_FAILURE);\
        }