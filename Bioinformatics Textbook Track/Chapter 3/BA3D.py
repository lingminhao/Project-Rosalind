k = 12
Text = 'TGTCGACGATGTGGCGCTTGATGGGGTGGAACGATAAGCTGAGAAGTGGCTCTGCGATAGGTACACGAAAATCCTAACTCTTGGGACGCTAGAGAGAACTGGAACAGATAAACTGACGACGCTGCCATTTGACACACCGCTCGCGGACTGGGCATCACCAACTGAAAGGTGTTCCACCGTGATAGTCGCGCTCCTTCCTGTGGGTAAACCAAGAGAGTATTGCACGTATTTTACGCCATACCCAGCCACGTAAGCACTAATTATATTGTAGCTAACTCGGGTCGCCTGGTTCACCCTGGTACGCCGGGCAGTAGTCCGCAATAGGATTCGTAATAGGTAATGAACTGGACCCAAAACGTAGTGATAGGCTTCCATATTGCGCACATCAGAAACGTCAGTGCCCGAAGGTGGACGTATTCATGTTGGATGCTCCATGGGGAATTCGAATTTATAGTATATGGGCCAGGCGCGCTTCCATAGCCCTGAAAGAGCTCACCGAAGTCACTGATTTCTTTACGTCGTCAGTAGGACGTGTGAGGCCCGATGCCCAATACTGGCTCGCTTGTGTATCGATGCCAGCTCAGATGACAAAAACATATGTGTCTGCATCCCTATCTCACCAATCGTACAGCGAGGACGGAAGGTAATGCGTGCGAGACATTCGTCGCAACGCAGGAGTCAACCCGAATAGACGGTCGGTGAGATCAGCTCCTCGACATTCAGACCCTTCTAAGTTAATCTCATGCTTCGGTGCCTCGCAGGAGTAGACGGTCGGCGTGTGATTCGACTAACAAACTCGCTGGGTAGGTCAACGTACTATAAGTTGACATCTCTGATCTGCACTGTTTTAATCCTACTTGTAAATTGGAGGCGGGTACGACGTGCTAACCTACTAGGGTCCAGTAGGTGTTGATGTTTGAGGCCATTTACTGATCAGCTAAGCCGTTGAGGATCAACTTTTACTCTCCAATAGTCCCAATTACGTTACTACACTTTTAGTATTAAACCCCGACTCCTAGAGCACTCTGAGTCCACAATAGGGGAATGGTACACCATCCCGTAAAGCAACGGAGTGACAATCGGCGTACGCATCCGCTTGATCGACTCGCGATGCCAAACAAGCGCACTGATCAGATCATGACGGGATATTTGATCGAGCAGCCCTCGTTCCTCCGCCTTCCCCTCGAGCCACAAGGGATGCTTGGTGAATCTCCCGTTCGGTACGCGTCCATTAAAGGGGAAGTTACCTATTCGAGCTTATGCTCCACATACTGTCTCCTGCGGCCCTACGCCCATCTCGACAGAACCCGTGGCGGACCTGAGCGACTCCCGGCCGATGGGTCGAAAACTTGTTGTAAGATCAAGTACTCAACCTGCCCACGGGACCAGCCAACCAGTATTCCGATCGATTTTACTTCCTGCTGACCCGTCGATGTCAACATCTAGGTAGCCGGCCTGCTGAGGATTGCTACAAACACCAGGAGGCTATGCATGAATGCGACATGCGAGGTCCAGTGAAGGGCAATGCCCTCTAAACTTTACTATACAAGCCTTGCTGTGCTCCACTTCAGATTAAAGTGCGATGAACATGCAAGAGCTATCCATAATGCAGGCAACCCAGGCTTTTATATCTATGGAACCTTAACCCTTTAACATCCCCGACCGTCGCCTGGCGTTACCCAGGGTGTGCTGCAGAGGTCCTCAGCCATTTTTTTGCTCCCATCGAAGCGAATGAGTGCGCCGTGTCATGCATTTGATCGGTCCACGTCAGAGCTACCGCATTGTTGGTCTAGGAAGATCACACCTGACGGAAGGCAGCCAACTCTGAGCTGCTTCTAACCTGTGACTCACCCCGTACAACGGGGCACCCCCCACTACCCCCGACGAATAGCTCAGGGCATATGCATGATTCTTACGTTCAATTATACCTTACATGACTTGCCCACCAGGGCGTGAGAGAGTCACCTCGAAACTGCCTACCTGGGTGTAACCATTGGAGA'

edge = []
node = []
node.append(Text[0:k-2])
for i in range(len(Text)-k+2):
    string = Text[i:i+k-1]
    edge.append(string)
    node.append(string[1:k])
origin = []
play = []
for i in range(len(node)-2):
    if edge[i] not in play:
        lst = [edge[i+1]] 
        for j in range(i+1,len(node)-2):
            if (node[i] == node[j]) & (node[i+1] == node[j+1]):
                lst.append(edge[j+1])
                lst.sort()
        add = edge[i] + ' -> ' + lst[0]
        for k in range(1,len(lst)):
            add = add + ',' + lst[k]
        origin.append(add)
    play.append(edge[i])

origin.sort()
for i in origin: print(i)