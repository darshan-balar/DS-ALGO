
#define COMPARE(x,y) (((x) < (y)) ? -1 : ((x) == (y)) ? 0 : 1)
int binarysearch(int *list, int n,int key)
{
    int middle,left=0,right=n-1;
    while(left<=right)
    {
        middle = (left+right)/2;
        switch(COMPARE(key,list[middle]))
        {
            case -1 : right = middle-1;
                    break;
            case 0 : return middle;
            case 1 : left = middle+1;
        }
    }
    return -1;
}