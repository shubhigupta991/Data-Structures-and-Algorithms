#include <iostream>
using namespace std;

int main() {
    char string[] = "WelcomE";
    int i;

    cout << "Old string : " << string << '\n';

    for(i = 0; string[i] != '\0'; i++) {
        if (string[i] >= 65 && string[i] <= 90)
            string[i] += 32;
        else if (string[i] >= 97 && string[i] <= 122)
            string[i] -= 32;
    }
    cout << "New string : " << string;

}
