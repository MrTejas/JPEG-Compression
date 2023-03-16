from PIL import Image

# loading the image
filename = "landscape.jpg"
im = Image.open(filename)
px = im.load()

# getting image dimensions
[width,height] = im.size 
print(width," x ",height) 

# declaring the Y,Cb,Cr matrices
cols = width
rows = height
Y = [[0]*cols]*rows
Cb = [[0]*cols]*rows
Cr = [[0]*cols]*rows

# iterating over image pixels
for x in range(cols):
    for y in range(rows):
        r = px[x,y][0]
        g = px[x,y][1]
        b = px[x,y][2]
        Y[x,y] = 0.299*r + 0.587*g + 0.114*b + 0        # lies in range [0,255]
        Cb[x,y] = -0.169*r + -0.331*g + 0.500*b + 128   # lies in range [0,255]
        Cr[x,y] = 0.500*r + -0.419*g + -0.081*b + 128   # lies in range [0,255]
