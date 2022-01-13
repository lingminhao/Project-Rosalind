with open('rosalind_ba1i.txt') as f:
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

def FrequentWordsWithMismatches(Text,k,d):
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
            FrequencyArray[i] = ApproximatePatternCount(Text,Pattern,d)
    maxcount = max(FrequencyArray)
    for i in range(4**k):
        if FrequencyArray[i] == maxcount: 
            FrequentPattern.append(NumbertoPattern(i,k))
    return FrequentPattern

L = FrequentWordsWithMismatches(Text,k,d)
with open('rosalind_ba1i_output.txt','w') as f:
    for i in range(len(L)):
        f.write(L[i])
        f.write('\n')
f.close()