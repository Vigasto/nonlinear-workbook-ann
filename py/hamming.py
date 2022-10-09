import numpy as np
import math

def distance(x,y):
    hamming_dist = (x==y)
    return (hamming_dist.size - sum(hamming_dist))

def main():
    x = np.array([1, -1, 1, 1])
    y = np.array([-1, 1, 1, -1])

    print(distance(x,y))

if __name__ == "__main__":
    main()