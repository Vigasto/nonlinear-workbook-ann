#include <iostream>

//signed binary hamming distance 
//-1 1 instead 1 0
int distance(int* x, int* y, int n) {
    int d = 0;
    for (int i=0; i<n; i++) {
        if (x[i]!=y[i])
            d++;
    }
    return d;
}

int main() {
    int n = 4;
    int* x = new int[n];
    x[0] =  1;
    x[1] = -1;
    x[2] =  1;
    x[3] =  1;

    int* y = new int[n];
    y[0] = -1;
    y[1] =  1;
    y[2] =  1;
    y[3] = -1;

    int result = distance(x,y,n);
    std::cout << "result = " << result << std::endl;

    delete[] x;
    delete[] y;
    
    return 0;
}