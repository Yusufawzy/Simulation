import random as r;import numpy as n ;import matplotlib.pyplot as plt
Labor_cost = Parts_Cost = Demand = profit = []
def Calc_Profit():
    c1 = Calc_Labor_Cost();Labor_cost.append(c1)
    c2 = Calc_Parts_Cost();Parts_Cost.append(c2)
    x  = Calc_Demand();Demand.append(x)
    p = (249-c1-c2)*x - 1000000
    profit.append(p);return p
def Calc_Labor_Cost():
    x = r.random()
    if   (x<0.1):return 43
    elif (x<0.3):return 44
    elif (x<0.7):return 45
    elif (x<0.9):return 46
    elif (x<1.0):return 47
def Calc_Parts_Cost(): return 80+r.random()*20
def Calc_Demand(): return n.random.normal(15000,4500)
def Plot ():
    plt.figure(1);plt.hist(Labor_cost,edgecolor='white');plt.title("Labor Cost Histogram")
    plt.figure(2);plt.hist(Parts_Cost,edgecolor='white');plt.title("Parts Cost Histogram")
    plt.figure(3);plt.hist(Demand,edgecolor='white');plt.title("Demand Histogram")
    plt.figure(4);plt.hist(profit, edgecolor='white');plt.title("Profit Histogram");
    plt.show(block=True)
def main(n):
    Loss_Count = Average_Profit = 0;Max_Profit = float('-inf');Min_Profit = float('inf')
    Labor_cost = Parts_Cost = Demand = profit = []
    for _ in range(n):
        Profit = Calc_Profit();Average_Profit+=Profit
        if (Profit <0):Loss_Count +=1
        Min_Profit=min(Profit,Min_Profit);Max_Profit=max(Profit,Max_Profit)
    Average_Profit = Average_Profit/n
    print("The maximum Profit is ",Max_Profit);print("The maximum Loss is ",abs(Min_Profit))
    print("The average Profit is ",Average_Profit);print("The probaility of loss is ",Loss_Count/n,"%")
    Plot()
main(10)
main(10000)
