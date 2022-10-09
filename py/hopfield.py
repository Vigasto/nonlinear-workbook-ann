import numpy as np
import math

def weights(W, x0, x1, x2):
    for i in range(x0.size):
        for j in range(x0.size):
            W[i][j] = x0[i]*x0[j] + x1[i]*x1[j] + x2[i]*x2[j]
    for k in range(x0.size):
        W[k][k] = 0

def mul(W,s,h):
    for i in range(s.size):
        sum = 0
        for j in range(s.size):
            sum += W[i][j]*s[j]
        h[i] = sum

def sign(y):
    return 1 if (y > 0) else -1

def check(v1, v2):
    isEqual = (v1==v2)
    return isEqual.all()

def energy(W, s):
    E = 0

    for i in range(s.size):
        for j in range(s.size):
            E += W[i][j]*s[i]*s[j]
    
    return -E

def main():
    N = 40

    x0 = np.array([
        -1, -1,  1, -1, -1,
        -1,  1,  1, -1, -1,
        -1, -1,  1, -1, -1,
        -1, -1,  1, -1, -1,
        -1, -1,  1, -1, -1,
        -1, -1,  1, -1, -1,
        -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1
    ])

    x1 = np.array([
        -1,  1,  1,  1, -1,
         1, -1, -1, -1,  1,
        -1, -1, -1, -1,  1,
        -1, -1,  1,  1, -1,
        -1,  1, -1, -1, -1,
         1, -1, -1, -1, -1,
         1,  1,  1,  1,  1,
        -1, -1, -1, -1, -1
    ])

    x2 = np.array([
         1, -1, -1,  1, -1,
         1, -1, -1,  1, -1,
         1, -1, -1,  1, -1,
         1,  1,  1,  1, -1,
        -1, -1, -1,  1, -1,
        -1, -1, -1,  1, -1,
        -1, -1, -1,  1, -1,
        -1, -1, -1, -1, -1
    ])

    W = np.zeros((40, 40))
    weights(W, x0, x1, x2)
    
    s = np.array([
         1,  1, -1,  1, -1,
        -1,  1, -1,  1,  1,
         1, -1, -1,  1, -1,
         1, -1,  1,  1,  1,
        -1, -1, -1, -1, -1
        -1, -1,  1,  1, -1,
        -1, -1, -1,  1, -1,
        -1, -1, -1, -1, -1
    ])

    E = energy(W,s)
    print(E)

    h = np.zeros(40)
    s1 = np.zeros(40)

    result = False
    count = 0
    
    while (count < 100 and result !=1):
        s1 = np.copy(s)
        mul(W,s,h)
        for j in range(s.size):
            if (h[j]!=0):
                s[j] = sign(h[j])
            if (h[j]==0):
                s[j] = s1[j]
        result = check(s,s1)
        count+=1
        print(count)
    
    print(s1)
    E = energy(W,s)
    print(E)

if __name__ == "__main__":
    main()