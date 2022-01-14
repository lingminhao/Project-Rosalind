import numpy as np

with open('input/rosalind_iev.txt') as f: 
    file = f.readlines()
    file = file[0].split()
    file = np.array([int(i) * 2 for i in file]) # to get number of offspring after a generation for each pairing
    
prob_dist = np.array([1,1,1,0.75,0.5,0]) # probability of getting dominant phenotype after a generation for each genotype.

answer = sum(file * prob_dist)

with open('output/rosalind_iev_output.txt', 'w') as f: 
    f.write(str(answer))
    
