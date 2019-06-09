import random as r;import matplotlib.pyplot as plt;MaxProfit = float('-inf');Res =0

#E(x) = 0.2*0+0.4*1+0.2*2+0.1*3+0.1*4
#E(x) = 1.5 PC/Wk

#Based on our previous analysis, the average demand of PCs was 1.5 PCs per week
#Then the owner should order almost 1.5 PCs per week
#The computer shop owner should order either 1 PC or 2 PCs each week

for n in range(1,3):
    Profit = avil = 0;arr = []
    for _ in range(500):
        avil +=n; #n will be 1 or 2
        demand = r.random();
        if (demand < 0.2):  demand = 0
        elif (demand < 0.6):  demand = 1
        elif (demand < 0.8):demand = 2
        elif (demand <0.9):demand = 3
        elif (demand < 1):demand = 4
        if (demand>avil): Profit-=(100*(demand-avil));Profit+=450*avil;avil=0
        elif (demand<avil): Profit-=(50*(avil-demand));Profit+=450*demand;avil-=demand;
        elif (demand==avil):Profit+=450*demand;avil=0
        arr.append(Profit);
    plt.hist(arr,edgecolor='white');plt.title("Profit")
    plt.show(block=True)
    print("Average Profit for ", n, " is ", Profit/500)
    if (MaxProfit<Profit):MaxProfit = Profit ; Res =n
print("The best Profit is achieved by Selling ",Res)













