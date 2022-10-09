#include <iostream>
#include <cmath>

int H(double* w, double* x, int n) {
    double sum = 0.0;
    for (int i=0; i<n; i++) {
        sum += w[i]*x[i];
    }
    return (sum >= 0.0);
}

int sign(double* w, double* x, int n){
    double sum = 0.0;
    for (int i=0; i<n; i++) {
        sum += w[i]*x[i];
    }
    return (sum >= 0.0);
}

double unipolar(double* w, double* x, int n){
    double lambda = 1.0;
    double sum = 0.0;
    for (int i=0; i<n; i++) {
        sum += w[i]*x[i];
    }
    return 1.0/(1.0 + exp(lambda*sum));
}

double bipolar(double* w, double* x, int n){
    double lambda = 1.0;
    double sum = 0.0;
    for (int i=0; i<n; i++) {
        sum += w[i]*x[i];
    }
    return tanh(lambda*sum);
}

int main() {
    int n = 5;
    double theta = 0.5;
    
    double* w = new double[n];
    w[0] = -theta;
    w[1] =  0.7;
    w[2] = -1.1;
    w[3] =  4.5;
    w[4] =  1.5;

    double* x = new double[n];
    x[0] =  1.0;
    x[1] =  0.7;
    x[2] =  1.2;
    x[3] =  1.5;
    x[4] = -4.5;

    int r1 = H(w,x,n);
    std::cout << "r1 = " << r1 << std::endl;
    int r2 = sign(w,x,n);
    std::cout << "r2 = " << r2 << std::endl;
    double r3 = unipolar(w,x,n);
    std::cout << "r3 = " << r3 << std::endl;
    double r4 = bipolar(w,x,n);
    std::cout << "r4 = " << r4 << std::endl;

    delete[] w;
    delete[] x;
    return 0;
}
