import itertools
with open('rosalind_ba6e.txt') as f:
    Text = f.readlines()
f.close()
Text = [x.strip() for x in Text]


kmerlength = int(Text[0])
string1 = Text[1] 
string2 = Text[2]


nucleotide = ['A','C','T','G']
lst = [''.join(p) for p in itertools.product(nucleotide, repeat = 9)]

def ReverseComplement(Pattern):
    lst = []
    newlst = []
    for i in range(len(Pattern)):
        lst.append(Pattern[len(Pattern)-i-1])
    for i in range(len(lst)):
        if lst[i] =='A': newlst.append('T')
        if lst[i] =='T': newlst.append('A')
        if lst[i] =='C': newlst.append('G')
        if lst[i] =='G': newlst.append('C')
    Reverse = ''.join(newlst)
    return Reverse


kmerlength = int(Text[0])
string1 = Text[1] 
string2 = Text[2]

lstofstring1name = []
lstofstring2name = []
lstofindex1name = []
lstofindex2name = []

for name in lst: 
    lstofstring1name.append(name)
    lstofstring2name.append(name)
    
    lstofindex1name.append(name)
    lstofindex2name.append(name)

lstofstring1name = lst[:]
lstofstring2name = lst[:]
lstofindex1name = lst[:]
lstofindex2name = lst[:]


string1dict = dict()
for name in lstofstring1name: 
    string1dict[name] = []
string2dict = dict()
for name in lstofstring2name: 
    string2dict[name] = []
index1dict = dict()
for name in lstofindex1name: 
    index1dict[name] = []

index2dict = dict()
for name in lstofindex2name: 
    index2dict[name] = []


for i in range(len(string1)-kmerlength+1): 
    substring = string1[i:i+kmerlength]
    string1dict[substring[0:9]].append(substring)
    index1dict[substring[0:9]].append(i)

for i in range(len(string2)-kmerlength+1): 
    substring = string2[i:i+kmerlength]
    string2dict[substring[0:9]].append(substring)
    index2dict[substring[0:9]].append(i)
        


with open('rosalind_ba6e_output.txt','w') as f: 
    for item in string1dict: 
        setstring1 = string1dict[item]
        for i in range(len(setstring1)): 
            start = setstring1[i][0:9]    
            end = ReverseComplement(setstring1[i])[0:9]
            for j in range(len(string2dict[start])): 
                if string1dict[item][i] == string2dict[start][j]:
                    f.write(str((index1dict[item][i],index2dict[start][j])))
                    f.write('\n')
            for j in range(len(string2dict[end])): 
                if ReverseComplement(string1dict[item][i]) == string2dict[end][j]:
                    f.write(str((index1dict[item][i],index2dict[end][j])))
                    f.write('\n')
f.close()
            
