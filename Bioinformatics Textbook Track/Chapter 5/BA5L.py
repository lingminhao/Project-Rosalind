from math import floor
import numpy as np
from Bio.SubsMat import MatrixInfo
matrix = MatrixInfo.blosum62
with open('rosalind_ba5l.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
v = Text[0]
w = Text[1]
def twocolumnweight(v,w,middle):
    sumofweight = np.zeros((len(v)+1,2))
    for i in range(len(v) + 1): 
        sumofweight[i,0] = -5*i
    if middle == 0: 
        sumofweight[0:len(v)+1,1] = sumofweight[0:len(v)+1,0] 
        return sumofweight
    count = 0
    while True:
        sumofweight[0,1] = sumofweight[0,0] - 5 
        for i in range(1,len(v)+1): 
            if (v[i-1],w[0]) in matrix: 
                sumofweight[i,1] = max(sumofweight[i,0]-5,sumofweight[i-1,1]-5,sumofweight[i-1,0] + matrix[(v[i-1],w[0])])
            else: 
                sumofweight[i,1] = max(sumofweight[i,0]-5,sumofweight[i-1,1]-5,sumofweight[i-1,0] + matrix[(w[0],v[i-1])])
        w = w[1:len(w)]
        count = count + 1
        if count == middle: 
            break
        sumofweight[0:len(v)+1,0] = sumofweight[0:len(v)+1,1] 
    return sumofweight

def MiddleNodeEdge(top, bottom, left, right): 
    a = v[top:bottom]
    b = w[left:right]
    middle = floor((left+right)/2) - left
    A = twocolumnweight(a,b,middle)
    fromsource = A[0:len(a)+1,1]
    # Tosink
    ar = a[::-1]
    br = b[::-1]
    middler = len(b) - middle
    Ar = twocolumnweight(ar,br,middler)
    tosink = np.flip(Ar[0:len(a)+1,1])
    length =  fromsource + tosink
    index = np.argmax(length)
    V = Ar[len(a)-index-1,1] -5 
    H = Ar[len(a)-index,0] -5
    if (ar[len(a)-index-1],br[middler-1]) in matrix: 
        D = Ar[len(a)-index-1,0] + matrix[(ar[len(a)-index-1],br[middler-1])] 
    else:
        D = Ar[len(a)-index-1,0] + matrix[(br[middler-1],ar[len(a)-index-1])] 
    if Ar[len(a)-index,1] == D: 
        return (index+top,'D')
    elif Ar[len(a)-index,1] == H:    
        return (index+top,'H')
    elif Ar[len(a)-index,1] == V:
        return (index+top,'V')

def LinearSpaceAlignment(top, bottom, left, right): 
    print([top, bottom, left, right])
    if left == right: 
        return 'V'*(bottom-top)
    if top == bottom: 
        return 'H'*(right-left)
    middle = floor((left+right)/2)
    midNode = MiddleNodeEdge(top, bottom, left, right)[0]
    midEdge = MiddleNodeEdge(top, bottom, left, right)[1] 
    pathL = LinearSpaceAlignment(top, midNode, left, middle)
    if midEdge == 'H' or midEdge == 'D': 
        middle = middle + 1
    if midEdge == 'V' or midEdge == 'D': 
        midNode = midNode + 1
    pathR  = LinearSpaceAlignment(midNode, bottom, middle, right)
    return pathL + midEdge + pathR

def RecovertheAlignment(path):
    v = Text[0]
    w = Text[1]
    vA = ''
    wA = ''
    score = 0
    for i in range(len(path)): 
        if path[i] == 'V': 
            vA = vA + v[0]
            wA = wA + '-'
            score = score - 5
            v = v[1:]
        elif path[i] == 'H': 
            vA = vA + '-'
            wA = wA + w[0]
            score = score - 5
            w = w[1:]
        elif path[i] == 'D' :
            vA = vA + v[0]
            wA = wA + w[0]
            if (v[0],w[0]) in matrix: 
                score = score + matrix[(v[0],w[0])]
            else: 
                score = score + matrix[(w[0],v[0])]
            v = v[1:]
            w = w[1:]
    return score, vA, wA

path = LinearSpaceAlignment(0,len(v),0,len(w))
for item in RecovertheAlignment(path):
    print(item)


