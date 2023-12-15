#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a[4]){
    int value =0;
    for(int i =0; i<=4;i++){
        if(value < a[i]){
            value = a[i];
        }
    }
    return value;
}

int main() {
    int a[4];
    scanf("%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);
    int ans = max_of_four(a);
    printf("%d", ans);
    
    return 0;
}

