import re
k = 30
d = 100

with open('rosalind_ba3j.txt') as f:
    List = f.readlines()
List = [x.strip() for x in List]
List1 = []

def Prefix(Text):
    return Text[0:len(Text)-1]
def Suffix(Text):
    return Text[1:len(Text)]

for i in range(len(List)):
    string = List[i]
    string1 = re.findall('([A-Z]+)|[A-Z]+', string)
    List1.append(string1)

List2 = []
for i in range(len(List1)):
    one = List1[i]
    for j in range(i+1,len(List1)):
       two = List1[j]
       if Suffix(one[0]) == Prefix(two[0]) and Suffix(one[1]) == Prefix(two[1]):
           List2.append([i,j])
       elif Prefix(one[0]) == Suffix(two[0]) and Prefix(one[1]) == Suffix(two[1]):
           List2.append([j,i])
List3 = []
for i in range(len(List2)):
    one = List2[i]
    appended = str(one[0]) + ' -> ' 
    for j in range(1,len(one)):
        appended = appended + str(one[j])
    List3.append(appended)
with open('practice2.txt','w') as g:
    for line in List3:
        g.write(line)
        g.write('\n')
g.close()


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
List4 = []
concatenate1 = List1[int(finalstring[0])][0]
concatenate2 = List1[int(finalstring[0])][1]
for i in range(len(finalstring)-1):
    node = List1[int(finalstring[i+1])]
    concatenate1 = concatenate1 + node[0][-1]
    concatenate2 = concatenate2 + node[1][-1]

finalans = concatenate1[0:k+d] + concatenate2
print(finalans)