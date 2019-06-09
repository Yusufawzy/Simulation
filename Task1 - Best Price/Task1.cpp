#include <bits/stdc++.h>
#include <time.h>
#include <cstdlib>
#define MaxPrice 100
typedef double dl;
int main(){
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator (seed); std::normal_distribution<double> Demand(1000,100);
    dl sales = 0 , revenue = 0 , avgRev , bestAvgRev = INT_MIN ; int bestPrice ;
    for (int price = 90 ; price <= MaxPrice ; price++){
        revenue = 0 ;
        for (int i = 0 ; i < 1000 ; i++){
            sales = Demand(generator) * powf (((float)price / 100),-2);
            revenue += sales * price ;
        }
        avgRev = revenue / 1000;
        std::cout<<"The average for price "<<price << " is "<<avgRev << std::endl;
        if (avgRev > bestAvgRev)bestAvgRev = avgRev , bestPrice = price;
    }
    printf("The Best Price is %d\n",bestPrice);
    system("pAUse");
}
