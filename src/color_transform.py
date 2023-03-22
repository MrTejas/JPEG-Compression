from PIL import Image
import numpy as np


# --------------------------------------------------------------------------------

# takes a rows x cols matrix (ar) and prints it
def printMatrix(rows,cols,ar):
    print("-------------------------")
    print("rows = "+str(rows))
    print("cols = "+str(cols))
    
    for x in range(rows):
        for y in range(cols):
            print(ar[x][y],end="\t")
        print("\n")        
    print("-------------------------")

# --------------------------------------------------------------------------------

# takes a rows x cols matrix (ar) and prints it
def printTupleMatrix(rows,cols,ar):
    print("-------------------------")
    print("rows = "+str(rows))
    print("cols = "+str(cols))
    
    for x in range(rows):
        for y in range(cols):
            print(str(ar[x,y]),end="\t")
        print("\n")        
    print("-------------------------")

# --------------------------------------------------------------------------------

# takes a rgb touple matrix and calculates 3 Y, Cb, Cr matrices
def colorConversion(rows,cols,ar):
    print("cols = "+str(cols))
    print("rows = "+str(rows))
    
    Y = [[0]*cols]*rows # creating a rows x cols matrix for Y
    Cb = [[0]*cols]*rows # creating a rows x cols matrix for Cb
    Cr = [[0]*cols]*rows # creating a rows x cols matrix for Cr

    # iterating over image pixels and printing them
    for x in range(rows):
        for y in range(cols):
            r = ar[x,y][0]
            g = ar[x,y][1]
            b = ar[x,y][2]

            Y[x][y] = int(0.299*r + 0.587*g + 0.114*b + 0  )      # lies in range [0,255]
            Cb[x][y] = int(-0.169*r + -0.331*g + 0.500*b + 128)   # lies in range [0,255]
            Cr[x][y] = int(0.500*r + -0.419*g + -0.081*b + 128)   # lies in range [0,255]
    
    print("Printing Y matrix : ")
    printMatrix(rows,cols,Y)


# --------------------------------------------------------------------------------

# takes a rgb touple matrix and calculates one rows x cols
# matrix of tuples containing Y,Cb,Cr values
def colorConversion2(rows,cols,ar):
    print("cols = "+str(cols))
    print("rows = "+str(rows))
    
    # creating a rows x cols tuple matrix initialized by (0,0,0)
    YCbCr = np.full((rows, cols, 3), (0, 0,0))
    
    # iterating over image pixels and printing them
    for x in range(rows):
        for y in range(cols):
            r = ar[x,y][0]
            g = ar[x,y][1]
            b = ar[x,y][2]

            Y = int(0.299*r + 0.587*g + 0.114*b + 0  )      # lies in range [0,255]
            Cb = int(-0.169*r + -0.331*g + 0.500*b + 128)   # lies in range [0,255]
            Cr = int(0.500*r + -0.419*g + -0.081*b + 128)   # lies in range [0,255]

            YCbCr[x,y][0] = Y
            YCbCr[x,y][1] = Cb
            YCbCr[x,y][2] = Cr
    

    print("Printing the color Transformed matrix : ")
    printTupleMatrix(rows,cols,YCbCr)


# --------------------------------------------------------------------------------


# loading the image
filename = "../images/pixel_landscape.jpg"
image = Image.open(filename)
px = image.load()
[rows,cols] = image.size 


print("rows = "+str(rows))
print("cols = "+str(cols))
print(image)
colorConversion2(rows,cols,px)

