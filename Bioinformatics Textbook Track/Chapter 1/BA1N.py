with open('rosalind_ba1n.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
Pattern = file[0]
d = int(file[1])

f.close()

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

with open('rosalind_ba1n_output.txt','w') as f:
    for i in Neighbors(Pattern,d):
        f.write(str(i))
        f.write('\n')

f.close()
