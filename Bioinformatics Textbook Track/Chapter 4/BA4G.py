from C4f import LeaderboardCyclopeptideSequencing

with open('practice.txt') as f: 
    Text = f.readlines()
Text = [x.strip().split(' ') for x in Text]
N = int(Text[0][0])
Spectrum = [int(x) for x in Text[1]]

print(LeaderboardCyclopeptideSequencing(Spectrum, N))




