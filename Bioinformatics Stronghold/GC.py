from Bio import SeqIO

sequence = SeqIO.parse('input/rosalind_gc.txt','fasta')



### START CODE HERE ###
dataset = []
for record in sequence:
    dataset.append(record)

opercentage = float(0)

for i in range(len(dataset)):
    G_content = dataset[i].seq.count('G') #dataset[i].seq gives the details of the record
    C_content = dataset[i].seq.count('C')
    percentage = float((G_content+C_content))/float(len(dataset[i].seq))*100
    if percentage > opercentage:
        opercentage = percentage
        datacode = dataset[i]
    else: 
        continue
### END CODE HERE ###

with open('output/rosalind_gc_output.txt', 'w') as f: 
    f.write(str(datacode.id) + '\n')  # get id from the dataset
    f.write(str(opercentage))