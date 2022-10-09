import numpy as np
import math

def H(w,x):
    return 1 if (np.sum(w*x) >= 0.0) else 0

def sign(w,x):
    return 1 if (np.sum(w*x) >= 0.0) else 0

def unipolar(w,x):
    lambda_var = 1.0
    return 1.0/(1.0 + math.exp(lambda_var*np.sum(w*x)))

def bipolar(w,x):
    lambda_var = 1.0
    return np.tanh(lambda_var*np.sum(w*x))

def main():
    theta = 0.5

    w = np.array([-theta, 0.7, -1.1, 4.5, 1.5])
    x = np.array([1.0, 0.7, 1.2, 1.5, -4.5])

    print(np.sum(w*x))

    print(H(w,x))
    print(sign(w,x))
    print(unipolar(w,x))
    print(bipolar(w,x))

if __name__ == "__main__":
    main()