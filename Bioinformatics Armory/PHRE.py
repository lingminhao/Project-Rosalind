from Bio import SeqIO

### START CODE HERE ###
count = 0
threshold = 20
for record in SeqIO.parse('input/rosalind_phre.txt','fastq'): 
    phred_quality = record.letter_annotations["phred_quality"]
    avg_quality = sum(phred_quality) / len(phred_quality)
    if avg_quality <= threshold: 
        count += 1
### END CODE HERE ###
   
with open('output/rosalind_phre_output.txt', 'w') as f: 
    f.write(str(count))

f.close()