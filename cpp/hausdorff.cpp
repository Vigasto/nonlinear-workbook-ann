#include <iostream>
#include <cmath>

double distance(double* x, double* y, int n){
    double result = 0.0;
    for(int j=0; j<n; j++){
        result += (x[j]-y[j])*(x[j]-y[j]);
    }
    return sqrt(result);
}

double dhausdorff(double** x, double** y, int p, int q, int n){
    double max = 0.0;
    double min, temp;
    for(int i=0; i<p; i++){
        min = distance(x[i],y[0],n);
        for(int j=0; j<q; j++){
            temp = distance(x[i], y[j], n);
            if (temp < min)
                min = temp;
            if (max < min)
                max = min;
        }
        return max;
    }
}

int main(void){
    int n = 2;
    int p = 3;
    int q = 2;

    double** X = NULL;
    X = new double*[p];
    
}