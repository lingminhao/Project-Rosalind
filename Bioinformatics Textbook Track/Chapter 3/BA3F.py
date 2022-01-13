import re
import random
with open('rosalind_ba3f.txt') as f:
    Text = f.readlines()
Text = [x.strip() for x in Text]

A = dict()
for i in range(len(Text)):
    string = Text[i]
    stuff1 = re.findall('([0-9]+) -> ',string)
    stuff2 = re.findall('[0-9]+ -> ([^ ]*)',string) #this is useful for data parsing
    stuff1 = stuff1[0]
    stuff2 = stuff2[0].split(',')
    A[stuff1] = stuff2

key = str(random.randint(0,len(A)-1))
lst = [key]
def Cycle(key):
    while True:
        if A[key] == []:
            break
        else:
            n = random.randint(0,len(A[key])-1)
            lst.append(A[key][n])
            key1 = key
            key = A[key][n]
            A[key1].remove(A[key1][n])
Cycle(key)

def Checker(lst):
    for key in lst:
        if A[key]!=[]:
            return 1

while Checker(lst) == 1: 
    for key in lst:
        if A[key] != []: 
            lst = lst[:len(lst)-1]
            lst1 = lst+lst
            lst1 = lst1[lst1.index(key):lst.index(key)+len(lst)]
            lst = lst1 + [lst1[0]]
            Cycle(key)
            break
cont = '->'.join(lst)
print(cont)