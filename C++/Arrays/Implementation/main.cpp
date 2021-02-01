#include <iostream>
using namespace std;

struct Array {
    int A[10];
    int size;
    int length;
};

void display(struct Array arr) {
    cout << "Elements of array are : " << endl;
    for(int i = 0; i < arr.length; i++) {
        cout << arr.A[i] << '\t';
    }
}
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
