
from C4f import Trim
from C4f import PeptidetoIM
with open('rosalind_ba4l.txt') as f: 
    Text = f.readlines()
Text = [x.strip().split(' ') for x in Text]
Leaderboard = Text[0]
LeaderboardIM = [PeptidetoIM(item) for item in Leaderboard]
Spectrum = [int(i) for i in Text[1]]
N = int(Text[2][0])

print(' '.join(Trim(Leaderboard, Spectrum, N)))