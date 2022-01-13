from math import floor
with open('input/rosalind_bins.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
lst = [int(i) for i in Text[2].split(' ')]
numbertosearch = [int(i) for i in Text[3].split(' ')]

### START CODE HERE ###
def BinarySearch(lst,item):
    left = 0
    right = len(lst)-1
    while left <= right: 
        mid = floor((left+right)/2)
        if lst[mid] == item: 
            return mid+1
        elif lst[mid] < item: 
            left = mid + 1
        else: 
            right = mid - 1
    return -1

finalanswer = []
for item in numbertosearch: 
    finalanswer.append(BinarySearch(lst,item))
finalanswer = [str(i) for i in finalanswer]
finalanswer = ' '.join(finalanswer)
### END CODE HERE ### 

with open('output/rosalind_bins_output.txt', 'w') as f: 
    f.write(finalanswer)