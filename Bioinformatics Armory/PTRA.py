from Bio.Seq import translate

with open('input/rosalind_ptra.txt') as f: 
    file = f.readlines()

file = [x.strip() for x in file]

DNAstring = file[0]
PROTstring = file[1]
f.close()

### START CODE HERE ### 
genetic_code_variant = [1,2,3,4,5,6,9,10,11,12,13,14,16,21,22,23,24,25,26,27,28,29,30,31,33]
output = 0 
for code_number in genetic_code_variant: 
    converted = translate(DNAstring, table=code_number, stop_symbol='*', to_stop=False)
    converted = converted[0:len(converted)-1]
    if converted == PROTstring:
        output = code_number
        break 

### END CODE HERE ###

with open('output/rosalind_ptra_output.txt', 'w') as f: 
    f.write(str(output))
    
f.close()