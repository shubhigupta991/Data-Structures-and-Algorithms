#include <iostream>
using namespace std;

float power(int x,int n) {
    if (n == 0) {
        return 1;
    }
    else
        return power(x,n-1) * x;
}

float fact(int x) {
    if (x == 0) {
        return 1;
    }
    else
        return fact(x-1) * x;
}

float taylor(int x, int n) {
    if (n == 0) {
        return 1;
    }
    else
        return taylor(x,n-1) + power(x,n)/fact(x);
}

int main() {
    cout << "Taylor Series : " << taylor(4,5);
}