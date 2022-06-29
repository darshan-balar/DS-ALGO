
#define COMPARE(x,y) (((x) < (y)) ? -1 : ((x) == (y)) ? 0 : 1)
int binarysearch(int *list, int left,int right,int key)
{
    int middle;
    if(left<=right)
    {
        middle = (left+right)/2;
        switch(COMPARE(key,list[middle]))
        {
            case -1 : return binarysearch(list,left,middle-1,key);
                    break;
            case 0 : return middle;
            case 1 : return binarysearch(list,middle+1,right,key);
        }
    }
    return -1;
}