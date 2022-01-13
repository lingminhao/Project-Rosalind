from C4f import LeaderboardCyclopeptideSequencing
from collections import Counter

with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
M = int(Text[0])
N = int(Text[1])
Spectrum = Text[2].split(' ')
Spectrum = [int(i) for i in Spectrum]
#A = ConvoSpectrum(Spectrum)
#A = A.split(' ')
#A = [int(i) for i in A]
#A = Counter(A)
#print(A)
#
#Counterkey = []
#for item in A.most_common(): 
#    Counterkey.append(item[0])
#a = A.get(Counterkey[M-1])
#print(a)
#
#newlst = A.copy()
#for key, values in A.items():
#    if A[key] < a: 
#        newlst.pop(key)
#A = newlst
#
#print(A)
#
#OnlyMass = []
#for key in A: 
#    if (57 <= key <=200) and (key not in OnlyMass):
#        OnlyMass.append(key)
#OnlyMass.sort()
#print(OnlyMass)
#

# This calculate the convolution spectrum between 57 and 200 ##
lst = []
for item1 in Spectrum: 
    for item2 in Spectrum:
        if (item2 > item1) and (57<=(item2-item1)<=200): 
            lst.append(item2-item1)

lst = Counter(lst)
print(lst)

## Find the most frequent elements between 57 and 200 (with ties) ##
Counterkey = []
for item in lst.most_common(): 
    Counterkey.append(item[0])
a = lst.get(Counterkey[M-1])

print(a)
newlst = lst.copy()
for key, values in lst.items():
    if lst[key] < a: 
        newlst.pop(key)
lst = newlst
print(lst)
# Form the new OnlyMass
OnlyMass = []
for key in lst: 
    if key not in OnlyMass: 
        OnlyMass.append(key)
OnlyMass.sort()
print(OnlyMass)

print(LeaderboardCyclopeptideSequencing(Spectrum, N))