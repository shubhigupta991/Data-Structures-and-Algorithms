#include <iostream>
using namespace std;

void TowerOfHanoi(int n, int A, int B, int C) {
    if (n > 0) {
        TowerOfHanoi(n-1,A,C,B);
        cout << "Tower " << A << " to " << "Tower " << C << endl;
        TowerOfHanoi(n-1,B,A,C);
    }
}

int main() {
    cout << "Tower of Hanoi with 3 disks" << endl;
    TowerOfHanoi(3,1,2,3);

    cout << "Tower of Hanoi with 5 disks" << endl;
    TowerOfHanoi(5,1,2,3);
}