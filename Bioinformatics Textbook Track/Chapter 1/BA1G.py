with open('rosalind_ba1g.txt') as f:
    file = f.readlines()
file = [x.strip() for x in file]
DNA1 = file[0]
DNA2 = file[1]

f.close()

def HammingDistance(DNA1,DNA2):
    count = 0
    for i in range(len(DNA1)):
        if DNA1[i]!=DNA2[i]:
            count = count+1
    return(count)

with open('rosalind_ba1g_output.txt','w') as f:
    f.write(str(HammingDistance(DNA1,DNA2)))

f.close()
