with open('rosalind_ba1c.txt') as f: 
    file = f.readlines()

file = [x.strip() for x in file]
Pattern = file[0]

f.close() 

### Start Code Here ###
def ReverseComplement(Pattern):
    lst = []
    newlst = []
    for i in range(len(Pattern)):
        lst.append(Pattern[len(Pattern)-i-1])
    for i in range(len(lst)):
        if lst[i] =='A': newlst.append('T')
        if lst[i] =='T': newlst.append('A')
        if lst[i] =='C': newlst.append('G')
        if lst[i] =='G': newlst.append('C')
    Reverse = ''.join(newlst)
    return Reverse
### End Code Here ###

with open('rosalind_ba1c_output.txt','w') as f: 
    f.write(ReverseComplement(Pattern))

f.close()