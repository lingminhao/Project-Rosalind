import re

lst1 = []
lst2 = []
lst3 = []


with open('input/rosalind_deg.txt') as f:
    Text = f.readlines()

Text = [x.strip() for x in Text]
Text.remove(Text[0])
f.close()

### START CODE HERE ###
for string in Text:
    firstnum = re.findall('([0-9]+) [0-9]+',string)
    lst1.append(int(firstnum[0]))
    secondnum = re.findall('[0-9]+ ([0-9]+)',string)
    lst2.append(int(secondnum[0]))

for i in range(len(lst1)):
    if lst1[i] not in lst3: 
        lst3.append(lst1[i])
    if lst2[i] not in lst3:
        lst3.append(lst2[i])
lst3.sort()

lst4 = [0]*(len(lst3))
for j in range(len(lst3)): 
    for i in range(len(lst1)):
        if lst3[j] == lst1[i]:
            lst4[j] = lst4[j] + 1
    for i in range(len(lst2)):
        if lst3[j] == lst2[i]:
            lst4[j] = lst4[j] + 1

lst4 = [str(i) for i in lst4]
lst4 = ' '.join(lst4)
### END CODE HERE ###

with open('output/rosalind_deg_output.txt', 'w') as f: 
    f.write(lst4)
f.close()