from Bio import Entrez
with open('input/rosalind_gbk.txt') as f: 
    lst = f.readlines()

lst = [x.strip() for x in lst]
genus = lst[0]
pub_start_date = lst[1]
pub_end_date = lst[2]

f.close()

sgenus = genus + '[Organism]'
spub_start_date = pub_start_date + '[Publication Date]'
spub_end_date = pub_end_date + '[Publication Date]'
subterm = sgenus + ' AND ' + spub_start_date + ':' + spub_end_date

Entrez.email = "lingminhao31@gmail.com"
handle = Entrez.esearch(db = "nucleotide", term = subterm) 
record = Entrez.read(handle)

with open('output/rosalind_gbk_output.txt','w') as f: 
    f.write(str(record["Count"]))
f.close()