with open('rosalind_ba1d.txt') as f: 
    file = f.readlines()
    
file = [x.strip() for x in file]
Pattern = file[0]
Genome = file[1]

f.close()

answer = []
for i in range(len(Genome)-len(Pattern)+1):
    if Genome[i:i+len(Pattern)]==Pattern:
        answer.append(i)

with open('rosalind_ba1d_output.txt','w') as f: 
    for item in answer: 
        f.write(str(item))
        f.write('\n')

f.close()