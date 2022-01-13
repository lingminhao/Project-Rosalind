from math import floor
import numpy as np
from Bio.SubsMat import MatrixInfo
matrix = MatrixInfo.blosum62
with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

v = Text[0]
w = Text[1]
middle = floor(len(w)/2)
def twocolumnweight(v,w,middle):
    sumofweight = np.zeros((len(v)+1,2))
    sumofweight[1:len(v)+1,0] = -5
    
    count = 0
    while True:
        sumofweight[0,1] = sumofweight[0,0] - 5
        for i in range(1,len(v)+1): 
            if (v[i-1],w[0]) in matrix: 
                sumofweight[i,1] = max(sumofweight[i,0]-5,sumofweight[i-1,1]-5,sumofweight[i-1,0] + matrix[(v[i-1],w[0])])
            elif (w[0],v[i-1]) in matrix: 
                sumofweight[i,1] = max(sumofweight[i,0]-5,sumofweight[i-1,1]-5,sumofweight[i-1,0] + matrix[(w[0],v[i-1])])
        w = w[1:len(w)]
        count = count + 1
        if count == middle: 
            break
        sumofweight[0:len(v)+1,0] = sumofweight[0:len(v)+1,1] 
    return sumofweight

# Fromsource
v = Text[0]
w = Text[1]
middle = floor(len(w)/2)
A = twocolumnweight(v,w,middle)
fromsource = A[0:len(v)+1,1]
# Tosink
vr = v[::-1]
wr = w[::-1]
middler = len(w) - middle
Ar = twocolumnweight(vr,wr,middler)
tosink = np.flip(Ar[0:len(v)+1,1])
length =  fromsource + tosink
index = np.argmax(length)
a = Ar[len(v)-index-1,1] -5 
b = Ar[len(v)-index,0] -5

if (vr[len(v)-index-1],wr[middler-1]) in matrix: 
    c = Ar[len(v)-index-1,0] + matrix[(vr[len(v)-index-1],wr[middler-1])] 
elif (wr[middler-1],vr[len(v)-index-1]) in matrix:
    c = Ar[len(v)-index-1,0] + matrix[(wr[middler-1],vr[len(v)-index-1])] 
if Ar[len(v)-index,1] == c: 
    print((index,middle), (index+1,middle+1))
elif Ar[len(v)-index,1] == b:    
    print((index,middle), (index,middle+1))
elif Ar[len(v)-index,1] == a:
    print((index,middle), (index+1,middle))
    