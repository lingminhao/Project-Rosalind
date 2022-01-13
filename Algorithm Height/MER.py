with open('input/rosalind_mer.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
lst1 = [int(i) for i in Text[1].split(' ')]
lst2 = [int(i) for i in Text[3].split(' ')]
f.close()

### START CODE HERE ###
def Merge(lst1, lst2):
    SortedList = []
    while lst1 != [] and lst2 != [] :
        if lst1[0] < lst2[0]: 
            SortedList.append(lst1[0])
            lst1.remove(lst1[0])
        else: 
            SortedList.append(lst2[0])
            lst2.remove(lst2[0])
    if lst1 == []: 
        SortedList = SortedList + lst2
    elif lst2 == []: 
        SortedList = SortedList + lst1
    SortedList = ' '.join([str(i) for i in SortedList])
    return SortedList
### END CODE HERE ###

with open('output/rosalind_mer_output.txt', 'w') as f: 
    f.write(Merge(lst1,lst2))
f.close()