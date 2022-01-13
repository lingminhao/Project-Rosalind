#def StringSpelledByGappedPatterns(GappedPatterns, k, d)：:
import re
k = 50
d = 200


with open('rosalind_ba3l.txt') as f:
    Text = f.readlines()
Text = [x.strip() for x in Text]

List = []
for i in range(len(Text)): 
    string = Text[i]
    string1 = re.findall('([A-Z]+)|[A-Z]+', string)
    List.append(string1)

def StringSpelledByGappedPatterns(List, k, d):
    FirstPattern = []
    SecondPattern = []
    for i in range(len(List)):
        FirstPattern.append(List[i][0])
        SecondPattern.append(List[i][1])
    
    PrefixString = FirstPattern[0]
    SuffixString = SecondPattern[0]
    for i in range(1,len(FirstPattern)):
        PrefixString = PrefixString + FirstPattern[i][-1]
        SuffixString = SuffixString + SecondPattern[i][-1]
        
    if any([PrefixString[i] != SuffixString[i-k-d] for i in range(k+d,len(PrefixString))]):
        message = "there is no string spelled by the gapped patterns"
        return message
    else:
        concatenate = PrefixString[0:k+d] + SuffixString
        return concatenate
    
        
print(StringSpelledByGappedPatterns(List, k, d))