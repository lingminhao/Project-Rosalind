from itertools import product
k = 9
Text = [''.join(p) for p in product('01', repeat=k)]
# ['111', '110', '101', '100', '011', '010', '001', '000']    
# sort by number of ones
Text.sort(key=lambda s: s.count('1'))
# ['000', '100', '010', '001', '110', '101', '011', '111']

########################## BA3E.py ##############################
A = dict()
def Prefix(Text):
    return Text[0:len(Text)-1]
def Suffix(Text):
    return Text[1:len(Text)]

for i in range(len(Text)):
    A[Prefix(Text[i])] = []
for i in range(len(Text)):
    B = A[Prefix(Text[i])]
    B.append(Suffix(Text[i]))
    B.sort()
lst = []
lines = []
for key in A:
    B = A[key]
    for i in range(len(B)):
        if key not in lst: 
            add = key + ' -> ' + B[i]
        else: add = add + ',' + B[i]
        lst.append(key)
    lines.append(add)

with open('practice.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
f.close()


########################## BA3F.py ################################    
import re
import random
with open('practice.txt') as f:
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
key = ''.join(['0']*(k-1))
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

############################# BA3B.py ################################
string1 = lst[0]
for i in range(len(lst)-1):
    string2 = lst[i+1]
    string1 = string1+string2[len(string2)-1]
print(string1[:-(k-1)])

