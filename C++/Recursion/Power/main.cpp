#include "iostream"
using namespace std;

int Power(int x, int p) {
    if (p == 0){
        return 1;
    }
    else
        return x * Power(x,p-1);
}

int main() {
    int a = Power(2,3);
    cout << a;
}