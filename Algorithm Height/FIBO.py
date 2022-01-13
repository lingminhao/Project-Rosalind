with open('input/rosalind_fibo.txt') as f: 
    file = f.readlines()

n = int(file[0])
f.close()

### START CODE HERE ###
a0 = 0
a1 = 1
count = 0
while count <= n - 2: #n-2
    a2 = a1 + a0
    a0 = a1
    a1 = a2
    count = count + 1
### END CODE HERE ###

with open('output/rosalind_fibo_output.txt', 'w') as f: 
    f.write(str(a2))
f.close()