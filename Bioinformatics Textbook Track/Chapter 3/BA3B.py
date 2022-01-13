
with open('rosalind_ba3b.txt') as f:
    Pattern = f.readlines()
Pattern = [x.strip() for x in Pattern]
print(Pattern)
k = 5
string1 = Pattern[0]
for i in range(len(Pattern)-1):
    string2 = Pattern[i+1]
    string1 = string1+string2[len(string2)-1]
print(string1)
        
        