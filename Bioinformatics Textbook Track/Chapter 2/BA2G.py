import random
from random import randint

k = 15
t = 20
N = 2000

with open('rosalind_ba2g.txt') as f: 
    Dna = f.readlines()
Dna = [x.strip() for x in Dna]

#Provide the Profile Matrix
def ProfileMatrix(List):
    Matrix = [0]*(len(List[0]))
    for i in range(len(List[0])):
        Count = [0,0,0,0]
        for j in range(len(List)):
            if List[j][i] == 'A': 
                Count[0] = Count[0]+1
            elif List[j][i] == 'C':
                Count[1] = Count[1]+1
            elif List[j][i] == 'G':
                Count[2] = Count[2]+1
            elif List[j][i] == 'T':
                Count[3] = Count[3]+1
        Matrix[i] = Count
    transposeMatrix=[list(e) for e in zip(*Matrix)]
    Count = transposeMatrix             
    lst = [sum(i) for i in zip(*Count)]
    for i in range(len(Count)):
        for l in range(len(Count[0])):
            Count[i][l] = Count[i][l]+1
    Profile = Count 
    for i in range(len(Count)):
        for l in range(len(Count[0])):
            Profile[i][l] = Count[i][l]/(4+lst[l])
    return Profile
#Provide the Count Matrix
def CountMatrix(List):
    Matrix = [0]*(len(List[0]))
    for i in range(len(List[0])):
        Count = [0,0,0,0]
        for j in range(len(List)):
            if List[j][i] == 'A': 
                Count[0] = Count[0]+1
            elif List[j][i] == 'C':
                Count[1] = Count[1]+1
            elif List[j][i] == 'G':
                Count[2] = Count[2]+1
            elif List[j][i] == 'T':
                Count[3] = Count[3]+1
        Matrix[i] = Count
    transposeMatrix=[list(e) for e in zip(*Matrix)]
    return transposeMatrix
#This function returns the scores of the profile matrix (with the consensus stirng)
def Score(Motif):
    scores = 0
    A=CountMatrix(Motif)
    transposeA = [list(e) for e in zip(*A)]
    for i in range(len(transposeA)):
        scores=scores+(len(Motif)-max(transposeA[i]))
    return scores

#Profile-randomly generated k-mer in the ith sequence. 
def Profilerandgen(Text,Profile):
    p =[]
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        product = 1
        for j in range(k):
            if Pattern[j] == 'A':
                product = product*Profile[0][j]
            elif Pattern[j] == 'C':
                product = product*Profile[1][j]
            elif Pattern[j] == 'G':
                product = product*Profile[2][j]
            elif Pattern[j] == 'T':
                product = product*Profile[3][j]
        p.append(product)
    p = [i/sum(p) for i in p]
    lst = [x for x in range(len(Text)-k+1)]
    rand = random.choices(lst,weights=p,k=1)
    return Text[rand[0]:rand[0]+k]

def GibbsSampler(Dna,k,t,N):
    Overall = []
    for i in range(20):
        Moti = []
        for i in range(len(Dna)):
            string = Dna[i]
            j= randint(0,len(Dna[0])-k)
            Moti.append(string[j:j+k])
        BestMotifs = Moti
        NewMoti = Moti
        for j in range(N):
            i = randint(0,t-1)
            del NewMoti[i]
            Profile = ProfileMatrix(NewMoti)
            NewMoti = NewMoti[0:i]+[Profilerandgen(Dna[i],Profile)]+NewMoti[i:]
            Motifs = NewMoti
            if Score(Motifs) < Score(BestMotifs):
                BestMotifs = Motifs[:] 
        Overall.append(BestMotifs)
    
    Scoring = []
    for i in range(20):
        Scoring.append(Score(Overall[i]))
    minimum = min(Scoring)
    A = Overall[Scoring.index(minimum)]
    
    return A

for i in GibbsSampler(Dna,k,t,N):
    print(i)