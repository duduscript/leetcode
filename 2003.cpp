#include <iostream>
#include <fstream>
#include <vecter>

using namespace std;

int main(){
    int h,n;
    fstream in("sample.txt");
    while(in>>n && n != 0){
        in >> h;
        vecter<int> ti(n-1),fi(n),di(n);
        for(int i=0;i!=n;++i) in >> fi[i];
        for(int i=0;i!=n;++i) in >> di[i];
        for(int i=0;i!=n-1;++i) in >> ti[i];
        int pos = 0,leave_time = h*5,leave_fish;
        while(leave_time - ti[pos] >= 0 || pos < n-1){
            leave_time -= ti[pos--];
        }
        int fish[] = new int[h*5];
        leave_fish = fi[pos];
        for(int i=leave_time;i!=h*5 && leave_fish > 0;++i){
            if(i == 0) fish[i] = leave_fish;
            else fish[i] = fish[i-1]+leave_fish-di[i];
        }
        for(int i=0;i!=h*5;++i) cout<<fish[i]<< " ";
        cout<<endl;
    }
    return 0;
}