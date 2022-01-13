#IntegerMass = [['G',57],['A',71],['S',87],['P',97],['V',99],
#                ['T',101],['C',103],['I',113],['L',113],['N',114],
#                ['D',115],['K',128],['Q',128],['E',129],['M',131],
#                ['H',137],['F',147],['R',156],['Y',163],['W',186]]
#
#Peptide = 'NQEL'
#
#PrefixMass = [0]*(len(Peptide)+1)
#for i in range(len(Peptide)):
#    for j in range(len(IntegerMass)):
#        if IntegerMass[j][0] == Peptide[i]:
#            PrefixMass[i+1] = PrefixMass[i] + IntegerMass[j][1]
#peptideMass = PrefixMass[len(Peptide)]
#print(PrefixMass)

#Method Similar to BA4C.py except the above modification. 