#Name : YUSUF FAWZY ELNADY
#ID   : 20160299

import numpy as n
MaxHours = 10;ProfitNet1 = 0;ProfitNet2 = 0;
for shop in range(2):
    TotalCost = 0; TotalSales = 0;
    for days in range (500):
        if (shop==0) : MaxWork = 2 ; MaxWait =1
        else : MaxWork = 6 ; MaxWait=9
        Waiting = []; ArrivalTime = 0;CompletionTime = []
        while (ArrivalTime<=MaxHours*60):
            IAT = n.random.normal(60/40,6/40)
            ArrivalTime += IAT
            for value in (CompletionTime) :
                if value <= ArrivalTime  :
                    CompletionTime.remove(value)
            if (len(CompletionTime)+len(Waiting)==MaxWait+MaxWork): continue
            if (len(CompletionTime)<MaxWork) :
                StartService = ArrivalTime
                ServiceTime = n.random.normal(6, 1)
                CompletionTime.append(ServiceTime+StartService)
                TotalSales += 22
            elif (len(Waiting)<MaxWait):
                TotalCost += (((min(CompletionTime))-ArrivalTime)*10) / 60
                StartService = (min(CompletionTime))
                Waiting.append(StartService)

            while(len(CompletionTime)<MaxWork and 0<len(Waiting)):
                ServiceTime = n.random.normal(6, 1)
                CompletionTime.append(Waiting[0]+ServiceTime)
                Waiting.remove(Waiting[0])
                TotalSales+=22
        if (shop==0) :
            TotalCost+=200+(20*MaxWork)
            ProfitNet1 += (TotalSales-TotalCost)
        else:
            TotalCost+=2000+(20*MaxWork)
            ProfitNet2 += (TotalSales-TotalCost)
print(sum)
ProfitNet1/=500;ProfitNet2/=500
if (ProfitNet1>ProfitNet2):
    print("Store 1 is the best")
else :
    print("Store 2 is the best")
