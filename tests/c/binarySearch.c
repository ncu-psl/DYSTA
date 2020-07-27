#include <stdlib.h>
#include <stdio.h>

int binarysearch(int *data, int key, int n){
    int low = 0;
    int high = n - 1;
    while (low <= high){
        int mid = (low + high) / 2;
        if (data[mid] == key){
            return  printf("Found index is %d\n", mid);
        }
        else if (data[mid] < key){
            low = (low + high)/2 + 1;
        }
        else if (data[mid] > key){
            high = (low + high)/2 - 1;
        }
        
    }
    return  printf("Not found\n");
}

int main(void){
    int data[1048576] = {0};
    data[0] = -1;
    binarysearch(data, -1, 1048576);
    return 1;
}
// low: 0  high: 131071
// real    0m0.002s
// user    0m0.000s
// sys     0m0.002s

/*
n = 1048576
real    0m0.006s
user    0m0.000s
sys     0m0.006s
*/

/* raspberry pi 3 model B v1.2 2015
n = 1048576
real    0m0.020s
user    0m0.009s
sys     0m0.011s
*/