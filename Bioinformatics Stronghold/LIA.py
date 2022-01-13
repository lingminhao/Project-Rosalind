with open('input/rosalind_lia.txt') as f: 
    file = f.readlines()

file = file[0].split(' ')
k = int(file[0])
N = int(file[1])

### START CODE HERE ### 
def factorial(k): 
    if k == 0: 
        return 1
    else: 
        return factorial(k-1) * k

def binomial(n,N,p): 
    return factorial(n) / (factorial(N) * factorial(n-N)) * p ** N * (1-p) ** (n-N)

sum = 0
n = 2**k

for i in range(N,n+1): 
    sum += binomial(n,i,0.25)

### END CODE HERE ###

with open('output/rosalind_lia_output.txt', 'w') as f: 
    f.write(str(round(sum,3)))