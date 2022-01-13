k=5
d=1

with open('rosalind_ba2a.txt') as f: 
    lst = f.readlines()
f.close()
lst = [x.strip() for x in lst]
k = int(lst[0][0])
d = int(lst[0][2])
Dna = lst[1:]

nucleotide = ['A','C','T','G']
def HammingDistance(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)
    
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

def NumbertoPattern(index,k):
    if k == 1:
        return nucleotide[index]
    prefixIndex = index//4
    r = index%4
    symbol = nucleotide[r]
    PrefixPattern = NumbertoPattern(prefixIndex,k-1)
    return PrefixPattern+symbol

def MotifEnumeration(Dna,k,d):
    List = []
    PossibleCand=[]
    for string in Dna:
        for i in range(len(string)-k+1):
            Pattern=string[i:i+k]
            for i in Neighbors(Pattern,d):
                if i not in PossibleCand:
                    PossibleCand.append(i)

    Count = [0]*(len(PossibleCand))
    for i in range(len(PossibleCand)): 
        for j in range(len(Dna)):
            string = Dna[j]
            for l in range(len(string)-k+1):
                if HammingDistance(PossibleCand[i],string[l:l+k])<=d: 
                    Count[i] = Count[i]+1
                    if Count[i]==j+1: break
            if Count[i] < j+1: break
    for i in range(len(Count)):
        if Count[i] == len(Dna):
            if PossibleCand[i] not in List:
                List.append(PossibleCand[i])
    
    return List

with open('rosalind_ba2a_output.txt','w') as f:
    for element in MotifEnumeration(Dna,k,d): 
        f.write(element + ' ')                
f.close()
                        
        
        
    
