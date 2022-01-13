from Bio import SeqIO

### START CODE HERE ###
count = 0
threshold = 22

phred_quality_sequences = []

for record in SeqIO.parse('input/rosalind_bphr.txt','fastq'): 
    phred_quality = record.letter_annotations["phred_quality"]
    phred_quality_sequences.append(phred_quality)

for i in range(len(phred_quality_sequences[0])): 
    sum = 0
    for j in range(len(phred_quality_sequences)): 
        sum = sum + phred_quality_sequences[j][i]
    if sum / len(phred_quality_sequences) < threshold: 
        count += 1

### END CODE HERE ###
   
with open('output/rosalind_bphr_output.txt', 'w') as f: 
    f.write(str(count))

f.close()