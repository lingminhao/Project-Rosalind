import numpy as np

Text = 'TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA'
k=6
A=[[0.364, 0.333, 0.303, 0.212, 0.121, 0.242],
[0.182, 0.182, 0.212, 0.303, 0.182, 0.303],
[0.121, 0.303, 0.182, 0.273, 0.333, 0.303],
[0.333, 0.182, 0.303, 0.212, 0.364, 0.152]]


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
    
    #Method 1 (To list)
    Answer = AbsDifference.index(min(AbsDifference))
    return Text[Answer:Answer+k]

print(Probable(Text,k,A))
