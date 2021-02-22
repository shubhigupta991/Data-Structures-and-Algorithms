#include <iostream>
using namespace std;

bool valid(char * s) {
    for(int i = 0; s[i] != '\0'; i++) {
        if (!(isalpha(s[i]) || isnumber(s[i])))
            return false;
    }
    return true;
}
int main() {
    char string1[] = "Anil123";
    char string2[] = "Ani$123";

    bool ans1 = valid(string1);
    bool ans2 = valid(string2);

    if (ans1 == true)
        cout << "Valid" << endl;
    else
        cout << "Invalid" << endl;

    if (ans2 == true)
        cout << "Valid" << endl;
    else
        cout << "Invalid" << endl;
    return 0;
}
