with open('rosalind_ba1m.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
index = int(file[0])
k = int(file[1])

f.close()

def NumbertoPattern(index,k):
    nucleotide = ['A','C','G','T']
    if k == 1:
        return nucleotide[index]
    prefixIndex = index//4
    r = index%4
    symbol = nucleotide[r]
    PrefixPattern = NumbertoPattern(prefixIndex,k-1)
    return PrefixPattern+symbol

with open('rosalind_ba1m_output.txt','w') as f:
    f.write(NumbertoPattern(index,k))

f.close()