#include "iostream"
using namespace std;

int Sum(int n) {
    if (n > 0) {
        return n + Sum(n-1);
    }
    else
        return 0;
}

int main() {
    int x = 10;
    int sum = Sum(x);
    cout << "Sum of first 10 natural numbers " << sum;
}
