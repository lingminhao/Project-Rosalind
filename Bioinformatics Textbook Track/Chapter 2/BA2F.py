from random import randint 

k = 15
t = 20
#
#Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
#'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
#'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
#'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

with open('rosalind_ba2f.txt') as f:
    Dna = f.readlines()
Dna = [x.strip() for x in Dna]

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

#This function computes the count matrix of a collection of motifs, which can be turned into profile matrix.
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


#This function compares the profile matrix with each string in Dna to find the most probable ones. 
def Motifs(Profile, Dna): 
    Motif = []
    for i in range(len(Dna)):
        string = Dna[i]
        Possible = Probable(string,k,Profile)
        Motif.append(Possible)
    return Motif

#This function returns the scores of the profile matrix (with the consensus stirng)
def Score(Motif):
    scores = 0
    A=CountMatrix(Motif)
    transposeA = [list(e) for e in zip(*A)]
    for i in range(len(transposeA)):
        scores=scores+(len(Motif)-max(transposeA[i]))
    return scores
#
def RandomizedMotifSearch(Dna,k,t):
    Moti = []
    for i in range(len(Dna)):
        string = Dna[i]
        j= randint(0,len(Dna[0])-k)
        Moti.append(string[j:j+k])
    BestMotifs = Moti
    while True: 
        Count = CountMatrix(Moti)             #This is the code to become Profile Matrix
        lst = [sum(i) for i in zip(*Count)]
        for i in range(len(Count)):
            for l in range(len(Count[0])):
                Count[i][l] = Count[i][l]+1
        Profile = Count 
        for i in range(len(Count)):
                    for l in range(len(Count[0])):
                        Profile[i][l] = Count[i][l]/(4+lst[l])
        if Score(Motifs(Profile, Dna))<Score(BestMotifs):
            BestMotifs = Motifs(Profile, Dna)
            Moti = Motifs(Profile,Dna)
        else:
            return BestMotifs #This part, there is a chance that for the later iterations , it might become smaller. 


lst = []   
lst2 = []     
for i in range(1000): 
    lst.append(RandomizedMotifSearch(Dna,k,t))
    lst2.append(Score(lst[i]))

for i in range(len(lst)):
    if lst2[i] == min(lst2):
        print(lst[i])
        for j in range(len(lst[i])):
            print(lst[i][j])
        print(Score(lst[i]))