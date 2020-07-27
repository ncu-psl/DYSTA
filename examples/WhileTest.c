int O_n_1(int n){
    int i = 0;
    int n = n;
    while (i<n){
        i++;
    }
}

int O_n_2(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            i++;
        }
    }
}

int O_n_3(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            n--;
        }
    }
}

int O_n_4(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            i++;
        }
        else{
            n--;
        }
    }
}

void O_logn_1(int n){
    int i = 0;
    int n = n;
    while (i<n){
        i*=2;
    }
}

void O_logn_2(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            i*=2;
        }
        else{
            n--;
        }
    }
}

void O_logn_3(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            i++;
        }
        else{
            n/=2;
        }
    }
}

void O_logn_4(int n){
    int i = 0;
    int n = n;
    while (i<n){
        if(1){
            i*=2;
        }
        else{
            n/=2;
        }
    }
}