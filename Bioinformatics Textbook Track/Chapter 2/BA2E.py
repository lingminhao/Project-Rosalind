with open('rosalind_ba2e.txt') as f:
    Dna = f.readlines()
Dna = [x.strip() for x in Dna]

k = 12
t = 25

def Probable(Text,k,Profile):
    probprofile = 1
    transposeProfile = [list(e) for e in zip(*Profile)]
    for i in range(len(transposeProfile)):
        probprofile=probprofile*max(transposeProfile[i])
        
    Count = []
    
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
        Count.append(product)
        
    Difference = [count - probprofile for count in Count]
    AbsDifference = [abs(difference) for difference in Difference]
    
    Answer = AbsDifference.index(min(AbsDifference))
    return Text[Answer:Answer+k]

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

def Score(Motifs):
    scores = 0
    A=CountMatrix(Motifs)
    transposeA = [list(e) for e in zip(*A)]
    for i in range(len(transposeA)):
        scores=scores+(len(Motifs)-max(transposeA[i]))
    return scores

        

def GreedyMotifSearch(Dna,k,t):
    BestMotifs =[]
    for string in Dna: 
        BestMotifs.append(list(string[0:k]))
    for i in range(len(Dna[0])-k+1):
        Motifs=[]
        kMerMotif = Dna[0][i:i+k]
        Motif1 = kMerMotif
        Motifs.append(Motif1)
        for j in range(1,t):
            Count = CountMatrix(Motifs)             #This is the code to become Profile Matrix
            lst = [sum(i) for i in zip(*Count)]
            for i in range(len(Count)):
                for l in range(len(Count[0])):
                    Count[i][l] = Count[i][l]+1
            ProfileMatrix = Count 
            for i in range(len(Count)):
                for l in range(len(Count[0])):
                    ProfileMatrix[i][l] = Count[i][l]/(4+lst[l])
            Motifs.append(Probable(Dna[j],k,ProfileMatrix))

        if Score(Motifs)<Score(BestMotifs):
            BestMotifs=Motifs
    return BestMotifs
        
L = GreedyMotifSearch(Dna,k,t)
for i in L: print(i)


