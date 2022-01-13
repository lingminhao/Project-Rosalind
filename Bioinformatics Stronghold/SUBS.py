with open('input/rosalind_subs.txt') as f: 
    file = f.readlines()

file = [x.strip() for x in file]
DNAstring1 = file[0]
DNAstring2 = file[1]
f.close()

### START CODE HERE ###
k = len(DNAstring2)

location = []
for i in range(len(DNAstring1) - k + 1): 
    if DNAstring1[i:i+k] == DNAstring2: 
        location.append(i)
### END CODE HERE ###
        
with open('output/rosalind_subs_output.txt', 'w') as f: 
    for number in location: 
        f.write(str(number+1))
        f.write(' ')
f.close()
