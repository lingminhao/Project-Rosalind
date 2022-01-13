with open('rosalind_ba3c.txt') as f:
    Pattern = f.readlines()
Pattern = [x.strip() for x in Pattern]

def Prefix(Text):
    return Text[0:len(Text)-1]
def Suffix(Text):
    return Text[1:len(Text)]


for i in range(len(Pattern)):
    for j in range(len(Pattern)):
        if j != i:
            if Suffix(Pattern[i])==Prefix(Pattern[j]):
                print(Pattern[i] + ' -> ' + Pattern[j])
            elif Suffix(Pattern[j])==Prefix(Pattern[i]):
                print(Pattern[j] + ' -> ' + Pattern[i])
        else: break

        