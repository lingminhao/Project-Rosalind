with open('rosalind_ba1h.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
Pattern = file[0]
Text = file[1]
d = int(file[2])

f.close()

def Ham(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)

answer = []
for i in range(len(Text)-len(Pattern)+1):
    if Ham(Text[i:i+len(Pattern)],Pattern)<=d:
        answer.append(i)

with open('rosalind_ba1h_output.txt','w') as f:
    for item in answer:
        f.write(str(item))
        f.write('\n')
f.close()