with open('rosalind_ba2b.txt') as f: 
    lst = f.readlines()
f.close()
lst = [x.strip() for x in lst]
k = int(lst[0])
Dna = lst[1:]

def HammingDistance(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)

def Neighbors(Pattern,d):
    nucleotide = ['A','T','C','G']
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

def NumbertoPattern(index,k):
    nucleotide = ['A','T','C','G']
    if k == 1:
        return nucleotide[index]
    prefixIndex = index//4
    r = index%4
    symbol = nucleotide[r]
    PrefixPattern = NumbertoPattern(prefixIndex,k-1)
    return PrefixPattern+symbol

def MedianString(Dna,k):
    final = []
    minCount = [0]*(4**k)
    for i in range(4**k):
        summation = 0
        Pattern = NumbertoPattern(i,k)
        for j in range(len(Dna)):
            string = Dna[j]
            lst = []
            for l in range(len(string)-k+1):
                lst.append(HammingDistance(Pattern,string[l:l+k]))
            summation = summation + min(lst)
        minCount[i] = summation
    for i in range(4**k):
        if minCount[i]==min(minCount): 
            final.append(NumbertoPattern(i,k))
    return final

k = MedianString(Dna,k)

with open('rosalind_ba2b_output.txt', 'w') as f: 
    for i in k: 
        f.write(i + ' ')
f.close()
