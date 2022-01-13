from Bio.Seq import Seq 
with open("input/rosalind_ini.txt") as f: 
    DNA = f.readline()
f.close()

nucleotide = ["A","C","G","T"]
my_seq = Seq(DNA)

with open("output/rosalind_ini_output.txt",'w') as f:
    for item in nucleotide: 
        f.write(str(my_seq.count(item)) + ' ')

f.close()