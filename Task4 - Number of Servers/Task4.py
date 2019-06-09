import numpy as np
W_Avg = float('inf') ; n = 0
while W_Avg > 0.5 :
    n+=1 ; AT = 0 ; W = 0 ; AvailTimeArray = [0]*n
    for i in range(1,1001):
        IAT = np.random.normal(0.6,0.1)
        AT += IAT
        MinValue = min(AvailTimeArray)
        Idx = AvailTimeArray.index(MinValue)
        if AT > MinValue : StartService = AT 
        else : StartService = MinValue
        W+=StartService-AT
        ST = np.random.normal(5,1)
        Completion = ST + StartService
        AvailTimeArray[Idx] = Completion
    W_Avg = W / 1000
print('Number of servers are ',n) 