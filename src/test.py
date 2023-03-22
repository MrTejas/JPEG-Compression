import numpy as np

ar = np.full((4, 3, 2), (1, 2))

for i in range(4):
    for j in range(3):
        print(ar[i,j][1],end="\t")
    print("\n")

    
