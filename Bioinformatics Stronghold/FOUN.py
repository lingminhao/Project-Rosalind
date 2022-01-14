import numpy as np
from math import comb

with open('input/rosalind_foun.txt') as f: 
    file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip().split()

N = int(file[0][0]) # number of individuals
m = int(file[0][1]) # number of generation passed
A = np.array([int(j) for j in file[1]]) # number of recessive alleles (for each factor)

# A function to get prob distribution of recessive alleles for generation i+1 from generation i (i>=2). 
def prob_genij(gen_before):
    gen_after = []
    for j in range(2 * N + 1): 
        total = 0 
        for i in range(2 * N + 1): 
            total += gen_before[i] * ((i / (2 * N)) ** j) * ((2*N - i) / (2*N)) ** (2*N - j) * comb(2*N, j)
        gen_after.append(total)
        j += 1
    return gen_after

def matrixBcolumn(m, factor_num_recessive): #
# m = number of generation to put
# factor_num_recessive = number of recessive alleles for a given factor
# return a column with the log probability of no recessive alleles remaining for each generation.
    column = []    
    p = factor_num_recessive / (2 * N)
    
    # Get the prob distribution of dominant alleles at 2nd generation
    gen2 = []
    for i in range(2 * N + 1): 
        prob = p ** i * (1-p) ** (2 * N - i) * comb(2*N, i)
        gen2.append(prob)
    
    column.append(gen2[0])
    
    gen_before = gen2
    for i in range(m-1): 
        gen_after = prob_genij(gen_before)
        column.append(gen_after[0])
        gen_before = gen_after
    
    column = np.array(column)
    return np.log10(column)

B = matrixBcolumn(m, A[0]).reshape(m, 1)
for i in range(1,len(A)): 
    B = np.append(B,matrixBcolumn(m, A[i]).reshape(m, 1), axis = 1)

with open('output/rosalind_foun_output.txt', 'w') as f: 
    for i in range(B.shape[0]): 
        for j in range(B.shape[1]): 
            f.write(str(B[i,j]) + ' ')
        f.write('\n')


    