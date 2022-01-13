from C4f import ConvoSpectrum

with open('rosalind_ba4h.txt') as f: 
    Text = f.readlines()
Text = [x.strip().split(' ') for x in Text]
Spectrum = Text[0]
Spectrum = [int(x) for x in Spectrum]
Spectrum.sort()


print(ConvoSpectrum(Spectrum))