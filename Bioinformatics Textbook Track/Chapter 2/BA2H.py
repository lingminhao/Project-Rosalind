
Pattern = 'GGCTAAT'
with open('rosalind_ba2h.txt') as f:
    Dna = f.read().split(' ')
Dna = [x.strip() for x in Dna] #to strip off everything in the list. 

print(Dna)

#Pattern = 'AAA'
#Dna = [']


def HammingDistance(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)
        
def DistanceBetweenPatternAndStrings(Pattern,Dna):
    k = len(Pattern)
    distance = 0
    for i in range(len(Dna)):
        Ham = 10000000000
        string = Dna[i]
        for j in range(len(string)-k+1):
            if HammingDistance(Pattern,string[j:j+k])<Ham:
                Ham = HammingDistance(Pattern,string[j:j+k]) 
        distance = distance + Ham
    return distance

print(DistanceBetweenPatternAndStrings(Pattern,Dna))
            