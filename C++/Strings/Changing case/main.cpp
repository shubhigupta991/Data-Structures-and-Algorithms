#include <iostream>
using namespace std;

int main() {
    char* string = "welcome";
    int i;

    cout << "Old string : " << string << '\n';

    for(i = 0; string[i] != '\0'; i++) {
        string[i] = string[i] + 32;
    }
    cout << "New string : " << string;

}
