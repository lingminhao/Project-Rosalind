with open('rosalind_ba1f.txt') as f:
    file = f.readlines()

file = [x.strip() for x in file]
Genome = file[0]

f.close()

lst =[0]
Skew = 0
for i in range(len(Genome)):
    if Genome[i]=='C':
        Skew=Skew-1
        lst.append(Skew)
    elif Genome[i]=='G':
        Skew=Skew+1
        lst.append(Skew)
    else: lst.append(Skew)

minimum = min(lst)
answer = []
for i in range(len(lst)):
    if lst[i]== minimum:
        answer.append(i)

with open('rosalind_ba1f_output.txt','w') as f:
    for item in answer:
        f.write(str(item))
        f.write('\n')

f.close()