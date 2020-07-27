#include <stdlib.h>
#include <stdio.h>
int linearsearch(unsigned *data, int key, unsigned n){
    for(unsigned i = 0; i < n; i++){
        // printf("i: %d\n", i);
        if(key == data[i]){
            return  printf("Found index is %d\n", i);
        }
    }
    return printf("Not found\n");
}

int main(int argc, int *argv){
    unsigned n = 1048576;
    unsigned data[1048576] = {0};
    data[1048576-1] = -1;
    linearsearch(data, -1, 1048576);
    return 1;
}
/*
n = 131072
real    0m0.003s
user    0m0.003s
sys     0m0.000s
*/

/*
n = 262144
real    0m0.005s
user    0m0.000s
sys     0m0.004s
*/

/*
n = 254288
real    0m0.008s
user    0m0.000s
sys     0m0.007s
*/

/*
n = 1048576
real    0m0.013s
user    0m0.009s
sys     0m0.004s
*/

/* raspberry pi 3 model B v1.2 2015
n = 1048576
real    0m0.055s
user    0m0.036s
sys     0m0.020s
*/



