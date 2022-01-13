with open('rosalind_ba6b.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
Text = Text[0].split(' ')
Text[0] = Text[0].split('(')
Text[0] = Text[0][-1]
Text[-1] = Text[-1].split(')')
Text[-1] = Text[-1][0]

P = len(Text)
for i in range(P): 
    if Text[i][0] == '-' : 
        Text[i] = -int(Text[i][1:])
    else: 
        Text[i] = int(Text[i][1:])
f.close()

Text.insert(0,0)
Text.append(P+1)

count = 0
for i in range(len(Text)-1): 
    if Text[i+1]-Text[i] != 1: 
        count = count + 1


with open('rosalind_ba6b_output.txt','w') as f: 
    f.write(str(count))
f.close()
