with open('rosalind_ba1l.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
Pattern = file[0]

f.close()

def PatterntoNumber(Pattern):
    lst = ['A','C','G','T']
    if Pattern == '':
        return 0
    symbols = Pattern[len(Pattern)-1]
    Prefix = Pattern[0:len(Pattern)-1]
    return 4*PatterntoNumber(Prefix)+lst.index(symbols) #Because every term in k-1 mers repeat 4 times due to ACGT.

with open('rosalind_ba1l_output.txt','w') as f:
    f.write(str(PatterntoNumber(Pattern)))

f.close()