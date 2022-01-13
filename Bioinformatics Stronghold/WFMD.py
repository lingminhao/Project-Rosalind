from math import comb 

with open('input/rosalind_wfmd.txt') as f: 
    file = f.readlines()
    file = file[0].split()
    
N = int(file[0])
m = int(file[1])
g = int(file[2])
k = int(file[3])


# Probability of recessive alleles 
p = (2*N - m) / (2 * N)


# Get the prob distribution of dominant alleles at 2nd generation
gen2 = []
for i in range(2 * N + 1): 
    prob = p ** i * (1-p) ** (2 * N - i) * comb(2*N, i)
    gen2.append(prob)

# A function to get prob distribution of recessive alleles for generation i+1 from generation i. 
def prob_genij(gen_before):
    gen_after = []
    for j in range(2 * N + 1): 
        total = 0 
        for i in range(2 * N + 1): 
            total += gen_before[i] * ((i / (2 * N)) ** j) * ((2*N - i) / (2*N)) ** (2*N - j) * comb(2*N, j)
        gen_after.append(total)
        j += 1
    return gen_after


# Use the function prob_genij to get prob distribution of recessive alleles at generation g. 
gen_before = gen2
for i in range(g - 1): 
    gen_after = prob_genij(gen_before)
    gen_before = gen_after
gen_final = gen_after

# Get the answer P(>=k recessive) = 1 - P(<= k-1 recessive)
answer = round(1 - sum(gen_final[:k]),3)

with open('output/rosalind_wfmd_output.txt', 'w') as f: 
    f.write(str(answer))
