with open('rosalind_ba1b.txt') as f: 
    file = f.readlines()
    
file = [x.strip() for x in file]
Text = file[0]
k = int(file[1])

f.close()

Count = []
lst = []
newlist = []

def PatternCount(Text,Pattern):
    count = 0
    for i in range(len(Text)):
        if Text[i:len(Pattern)+i]==Pattern:
            count = count+1
    return(count)
    
for i in range(len(Text)-k+1):
    Count.append(PatternCount(Text,Text[i:i+k]))
maxcount = max(Count)
for i in range(len(Text)-k+1):
    if Count[i] == maxcount:
        lst.append(Text[i:i+k])
for i in range(len(lst)):
    if lst[i] not in newlist:
        newlist.append(lst[i])

with open('rosalind_ba1b_output.txt','w') as f: 
    for item in newlist: 
        f.write(item)
        f.write('\n')

f.close()