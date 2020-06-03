// #include <complex.h>
// #include <math.h>
#define PI acos(-1)

int fft(int *a, int n){
    for (int m = 2; m <= n; m *= 2){
    int mh = m >> 1;
        for (int i = 0; i < mh; ++i){
            // double _Complex w = cos((2*PI)/m*i)-I*sin((2*PI)/m*i);
            for (int j = i; j < n; j += mh){
                int k = j + mh;
                int x = a[j] - a[k];
                a[j] += a[k];
                a[k] = w * x;
            }
        }
    }
  return a;
}
