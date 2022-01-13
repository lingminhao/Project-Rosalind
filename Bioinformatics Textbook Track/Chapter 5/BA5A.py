import numpy as np
with open('rosalind_ba5a.txt') as f: 
    Text = f.readlines()
Text = [x.strip() for x in Text]
money = int(Text[0])
coins = [int(i) for i in Text[1].split(',')]

def DPChange(money, coins): 
    lst = np.eye(len(coins))
    MinNumcoins = [0]*(money+1)
    numofCoins = np.zeros((money+1,len(coins)))
    for m in range(1,money+1): 
        MinNumcoins[m] = 99999999999999999999
        for i in range(len(coins)): 
            if m >= coins[i]: 
                if  MinNumcoins[m-coins[i]] + 1 < MinNumcoins[m]:
                    MinNumcoins[m] = MinNumcoins[m-coins[i]] + 1
                    numofCoins[m] = numofCoins[m-coins[i]] + lst[i]
    numofCoins = [int(i) for i in range(len(numofCoins)) for j in range(len(numofCoins[0]))]              
    return {'mininum number of coins': MinNumcoins[money], 'list of coins': numofCoins}

print(DPChange(money,coins))