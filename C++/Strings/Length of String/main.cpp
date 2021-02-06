#include <iostream>
using namespace std;

int main() {
    char* string = "welcome";
    int i;

    for(i = 0; string[i] != '\0'; i++);

    cout << "Length of string is " << i;
}