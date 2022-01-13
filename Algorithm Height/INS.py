## Insertion sort is useful when the size of list is small or when the 
## data is nearly sorted. 

with open('input/rosalind_ins.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
lst = [int(i) for i in Text[1].split(' ')]
f.close()

### START CODE HERE ###
count = 0
def InsertionSort(lst):
    count = 0
    for i in range(1,len(lst)):
        k = i
        while k >=1 and lst[k] < lst[k-1]: 
            replacement = lst[k]
            lst[k] = lst[k-1]
            lst[k-1] = replacement
            count = count + 1
            k = k-1 
    return count  
### END CODE HERE ###

with open('output/rosalind_ins_output.txt', 'w') as f: 
    f.write(str(InsertionSort(lst)))
f.close()