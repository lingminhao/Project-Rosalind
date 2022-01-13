with open('input/rosalind_hamm.txt') as f: 
    file = f.readlines()
file = [x.strip() for x in file]

### START CODE HERE ###
DNAstring1 = file[0]
DNAstring2 = file[1]

DNAstring1 = list(DNAstring1)
DNAstring2 = list(DNAstring2)

count = 0

for i in range(len(DNAstring1)):
    if DNAstring1[i]==DNAstring2[i]:
        continue
    else: count = count + 1
### END CODE HERE ###

with open('output/rosalind_hamm_output.txt', 'w') as f:  
    f.write(str(count))