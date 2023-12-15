#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size; 
    scanf("%d",&size); 
    size = size;
    int arr[size]; 
    
    for(int i = 0 ; i< size; i++){
        scanf("%d",&arr[i]);
    }
    
    for(int i2 = size-1; i2>=0; i2--){
        cout<<arr[i2]<<" ";
    }
}
