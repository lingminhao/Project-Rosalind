with open('rosalind_ba1j.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
Text = file[0]
k = int(file[1].split(' ')[0])
d = int(file[1].split(' ')[1])

f.close()

nucleotide = ['A','C','T','G']
def HammingDistance(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)

def ApproximatePatternCount(Text,Pattern,d):
    count=0
    for i in range(len(Text)-len(Pattern)+1):
        Pattern2 = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern,Pattern2)<=d:
            count = count + 1
    return count 

def NumbertoPattern(index,k):
    if k == 1:
        return nucleotide[index]
    prefixIndex = index//4
    r = index%4
    symbol = nucleotide[r]
    PrefixPattern = NumbertoPattern(prefixIndex,k-1)
    return PrefixPattern+symbol

def PatterntoNumber(Pattern):
    if Pattern == '':
        return 0
    symbols = Pattern[len(Pattern)-1]
    Prefix = Pattern[0:len(Pattern)-1]
    return 4*PatterntoNumber(Prefix)+nucleotide.index(symbols)

def Neighbors(Pattern,d):
    if d==0:
        return [Pattern]
    if len(Pattern)==1:
        return nucleotide
    Nbhd = []
    SuffixNb = Neighbors(Pattern[1:len(Pattern)],d)
    for Text in SuffixNb:
        if HammingDistance(Pattern[1:len(Pattern)],Text)<d:
            for gene in nucleotide:
                add = gene+Text
                Nbhd.append(add)
        elif HammingDistance(Pattern[1:len(Pattern)],Text)==d:
            add = Pattern[0]+Text
            Nbhd.append(add)
    return Nbhd

def ReverseComplementProblem(Pattern):
    lst = []
    newlst = []
    for i in range(len(Pattern)):
        lst.append(Pattern[len(Pattern)-i-1])
    for i in range(len(lst)):
        if lst[i] =='A': newlst.append('T')
        if lst[i] =='T': newlst.append('A')
        if lst[i] =='C': newlst.append('G')
        if lst[i] =='G': newlst.append('C')
    A = ''.join(newlst)
    return A

def FrequentMismatchandComplement(Text,k,d):
    FrequentPattern = []
    Close = [0]*(4**k)
    FrequencyArray = [0]*(4**k)
    for i in range(len(Text)-k+1):
        Neighbourhood = Neighbors(Text[i:i+k],d)
        for Pattern in Neighbourhood: 
            index = PatterntoNumber(Pattern)
            Close[index] = 1
    for i in range(4**k):
        if Close[i] == 1: 
            Pattern = NumbertoPattern(i,k)
            FrequencyArray[i] = ApproximatePatternCount(Text,Pattern,d)+ApproximatePatternCount(Text,ReverseComplementProblem(Pattern),d)
    maxcount = max(FrequencyArray)
    for i in range(4**k):
        if FrequencyArray[i] == maxcount: 
            FrequentPattern.append(NumbertoPattern(i,k))
    return FrequentPattern

with open('rosalind_ba1j_output.txt','w') as f:
    for i in FrequentMismatchandComplement(Text,k,d):
        f.write(i)
        f.write('\n')
f.close()