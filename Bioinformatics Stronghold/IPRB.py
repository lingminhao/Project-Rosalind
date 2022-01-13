with open('input/rosalind_iprb.txt') as f: 
    file = f.readline()
file = file.split(' ')

k = int(file[0])
m = int(file[1])
n = int(file[2])
f.close()

### START CODE HERE ### 
branch1 = k/(k+m+n)
branch2 = (m/(k+m+n))*(k/(k+m+n-1))+(m/(k+m+n))*((m-1)/(k+m+n-1))*0.75+(m/(k+m+n))*(n/(k+m+n-1))*0.5
branch3 = (n/(k+m+n))*(k/(k+m+n-1))+(n/(k+m+n))*(m/(k+m+n-1))*0.5

p = branch1+branch2+branch3

### END CODE HERE ###

with open('output/rosalind_iprb_output.txt', 'w') as f: 
    f.write(str(p))

f.close()