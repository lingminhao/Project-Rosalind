with open('input/rosalind_ba7a.txt') as f: 
   file = f.readlines()

# Parse the data 
n = int(file[0])

file = file[1:]
m = len(file) 

root = []
leaves = []

count = []
for i in range(m): 
    count.append(int(file[i][3]))

counts = dict()
for i in count:
  counts[i] = counts.get(i, 0) + 1
  
print(counts)
for key in counts: 
    if counts[key] > 1: 
        root.append(key)
    else: 
        leaves.append(key)
        
print(root)
print(leaves)


# Determine the leaves