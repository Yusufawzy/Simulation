#include <iostream>
#include <iomanip>
#include <string>
#include <random>

using namespace std;

double getnumber(double m , double s)
{
        std::default_random_engine generator;
        std::normal_distribution<double> distribution(m,s);
        double r = distribution(generator);
        return r;
}

int main()
{
    int waitingjobs=0,breaktime=0;
    double Next_Failure=0;
    int max_jobs=100000,MachineAvailTime=0;
    double AT[100000],Time_in_system[100000];
    double Start_Service,Completion;
    for (int i = 0; i < 100000; i++)
     {
         AT[i] = 0;
         Time_in_system[i]=0;
     }
    for(int i=0; i<100000; i++)
    {
        Start_Service=0,Completion=0;
        double IAT = getnumber(1.25,0.2);
        if(i>1)
        {
            AT[i]=IAT+AT[i-1];
        }
        else
        {
            AT[i]=IAT;
        }


        if(AT[i]>MachineAvailTime)
        {
            Start_Service=AT[i];
        }
        else
        {
            Start_Service=MachineAvailTime;
            waitingjobs++;
        }

        if(Next_Failure==0)

        {
            Next_Failure = getnumber(450,50);
        }

        if (Start_Service>Next_Failure)
        {
            breaktime++;
            double repair_time = getnumber(60,5);

            Start_Service=Next_Failure+repair_time;
            waitingjobs++;
            Next_Failure=Start_Service+getnumber(450,50);
        }
        double Service_Time = 1;
        Completion = Start_Service+Service_Time;
        MachineAvailTime = Completion;
        Time_in_system[i] = Completion - AT[i];
    }
    double Avg_T=0;
    for(int i=0; i<100000; i++)
        Avg_T+=Time_in_system[i];
    Avg_T/=100000;
    cout<<"Number of jobs will have to wait in the system: "<<waitingjobs<<endl;
    cout<<"Average time jobs will spend in the system: "<<Avg_T<<endl;
    cout<<"Number of times the machine will breakdown: "<<breaktime<<endl;


    return 0;
}
