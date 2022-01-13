
import re
import random
#### Parsing data
with open('practice2.txt') as f:
    Text = f.readlines()
Text = [x.strip() for x in Text]

Counter1 = []
Counter2 = []
A = dict()
for i in range(len(Text)):
    string = Text[i]
    stuff1 = re.findall('([0-9]+) -> ',string)
    stuff2 = re.findall('[0-9]+ -> ([^ ]*)',string) #this is useful for data parsing
    stuff1 = stuff1[0]
    if stuff1 not in Counter1:
        Counter1.append(stuff1)
    stuff2 = stuff2[0].split(',')
    for stuff in stuff2: 
        if stuff not in Counter2: 
            Counter2.append(stuff)
    Counter1.sort(key = int)
    Counter2.sort(key = int)
    A[stuff1] = stuff2

cleaned = Counter2
for i in range(len(Counter1)):
    if Counter1[i] not in cleaned:
        cleaned.append(Counter1[i])
cleaned.sort()
Match = [0,0]
#####
def MatchOuterInner(A):
    #### This count the number of edges going out
    Outernode = [0]*(len(cleaned))
    for i in range(len(cleaned)):
        if cleaned[i] in Counter1:
            Outernode[i] = len(A[cleaned[i]])
        else: 
            Outernode[i] = 0
    ### This count the number of edges going in
    Innernode = [0]*(len(cleaned))
    for key in A: 
        for i in A[key]:
            Innernode[cleaned.index(i)] = Innernode[cleaned.index(i)]+1
    #### This find which nodes are unbalanced and add a path into dictionary
    for i in range(len(Outernode)):
        if Outernode[i] < Innernode[i]:
            Match[0] = cleaned[i]
        elif Outernode[i] > Innernode[i]:
            Match[1] = cleaned[i]
    if Match[0] not in A:
        A[Match[0]] = [Match[1]]
    else: 
        A[Match[0]]= A[Match[0]] + [Match[1]]

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

def Checker(lst):
    for key in lst:
        if A[key]!=[]:
            return 1
#####
MatchOuterInner(A)
key = random.choice(list(A))
lst = [key]
Cycle(key)
while Checker(lst) == 1: 
    for key in lst:
        if A[key] != []: 
            lst = lst[:len(lst)-1]
            lst1 = lst+lst
            lst1 = lst1[lst1.index(key):lst.index(key)+len(lst)]
            lst = lst1 + [lst1[0]]
            Cycle(key)
            break
        
lst = lst[:len(lst)-1]
lst1 = lst+lst
for i in range(len(lst1)):
   if (lst1[i] == Match[1]):
        string = lst1[i:i+len(lst)]
        if string[-1] == Match[0]:
            cont = '->'.join(string)
            print(cont)


































######################### BA3G.py #############################

import re
import random
#### Parsing data
with open('practice2.txt') as f:
    Text = f.readlines()
Text = [x.strip() for x in Text]

Counter1 = []
Counter2 = []
A = dict()
for i in range(len(Text)):
    string = Text[i]
    stuff1 = re.findall('([0-9]+) -> ',string)
    stuff2 = re.findall('[0-9]+ -> ([^ ]*)',string) #this is useful for data parsing
    stuff1 = stuff1[0]
    if stuff1 not in Counter1:
        Counter1.append(stuff1)
    stuff2 = stuff2[0].split(',')
    for stuff in stuff2: 
        if stuff not in Counter2: 
            Counter2.append(stuff)
    Counter1.sort(key = int)
    Counter2.sort(key = int)
    A[stuff1] = stuff2

cleaned = Counter2
for i in range(len(Counter1)):
    if Counter1[i] not in cleaned:
        cleaned.append(Counter1[i])
cleaned.sort()
Match = [0,0]
#####
def MatchOuterInner(A):
    #### This count the number of edges going out
    Outernode = [0]*(len(cleaned))
    for i in range(len(cleaned)):
        if cleaned[i] in Counter1:
            Outernode[i] = len(A[cleaned[i]])
        else: 
            Outernode[i] = 0
    ### This count the number of edges going in
    Innernode = [0]*(len(cleaned))
    for key in A: 
        for i in A[key]:
            Innernode[cleaned.index(i)] = Innernode[cleaned.index(i)]+1
    #### This find which nodes are unbalanced and add a path into dictionary
    for i in range(len(Outernode)):
        if Outernode[i] < Innernode[i]:
            Match[0] = cleaned[i]
        elif Outernode[i] > Innernode[i]:
            Match[1] = cleaned[i]
    if Match[0] not in A:
        A[Match[0]] = [Match[1]]
    else: 
        A[Match[0]]= A[Match[0]] + [Match[1]]

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

def Checker(lst):
    for key in lst:
        if A[key]!=[]:
            return 1
#####
MatchOuterInner(A)
key = random.choice(list(A))
lst = [key]
Cycle(key)
while Checker(lst) == 1: 
    for key in lst:
        if A[key] != []: 
            lst = lst[:len(lst)-1]
            lst1 = lst+lst
            lst1 = lst1[lst1.index(key):lst.index(key)+len(lst)]
            lst = lst1 + [lst1[0]]
            Cycle(key)
            break
        
lst = lst[:len(lst)-1]
lst1 = lst+lst
for i in range(len(lst1)):
   if (lst1[i] == Match[1]):
        string = lst1[i:i+len(lst)]
        if string[-1] == Match[0]:
            finalstring = lst1[i:i+len(lst)]
print(finalstring)
List4 = []
for i in range(len(finalstring)-1):
    value1 = finalstring[i]
    value2 = finalstring[i+1]
    node1 = List1[int(value1)]
    node2 = List1[int(value2)]
    concatenate1 = node1[0] + node2[0][-1]
    concatenate2 = node1[1] + node2[1][-1]
    List4.append([concatenate1,concatenate2])

final1 = List4[0][0]
print(final1)
final2 = List4[0][1]
print(final2)
for i in range(1,len(List4)):
    final1 = final1 + List4[i][0][-1]
    final2 = final2 + List4[i][1][-1]

print(final1 + final2[k+d:])