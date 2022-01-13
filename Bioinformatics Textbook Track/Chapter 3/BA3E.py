with open('rosalind_ba3e.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]

Text.sort()
k = 4
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
for key in A:
    B = A[key]
    for i in range(len(B)):
        if key not in lst: 
            add = key + ' -> ' + B[i]
        else: add = add + ',' + B[i]
        lst.append(key)
    print(add)

