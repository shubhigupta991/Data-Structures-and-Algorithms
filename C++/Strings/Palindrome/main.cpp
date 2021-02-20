#include <iostream>
using namespace std;

int main() {
    char string[] = "malayalam";
    int k = 1;
    int i,j;
    for (j = 0; string[j] != '\0'; j++);
    j = j - 1;
    for(i = 0; i < j; i++,j--) {
        if(string[i] != string[j]) {
            k = 0;
            break;
        }
    }
    if (k == 1)
        cout << "Its a palindrome";
    else
        cout << "Not a palindrome";
    return 0;
}
