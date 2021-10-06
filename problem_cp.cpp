#include <iostream>
using namespace std;

int main(){
    int n;
    int k=0;
    int k2=0;
    //cout<<"enter the size of 2d array"<<endl;
    cin>>n;
    int arr[n][n]={0};
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
            
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(i==j){
                k2+=arr[i][j];
            }
        }
    }
    //cout<<k2<<endl;
    for(int i=0;i<n;i++){
        for(int j=n;j>=0;j--){
            if(i+j==n-1){
               k+=arr[i][j];
            }
            
        }
    }
    cout<<abs(k2-k);


    
    
    return 0;
    
}