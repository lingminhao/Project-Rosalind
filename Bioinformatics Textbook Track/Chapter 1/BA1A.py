with open('rosalind_ba1a.txt') as f: 
    file = f.readlines()
    
file = [x.strip() for x in file]
Text = file[0]
Pattern = file[1]

f.close()

count = 0
newcount = 0
for i in range(len(Text)):
    if Text[i:len(Pattern)+i]== Pattern:
        count = count+1

with open('rosalind_ba1a_output.txt','w') as f: 
    f.write(str(count))
    
f.close()