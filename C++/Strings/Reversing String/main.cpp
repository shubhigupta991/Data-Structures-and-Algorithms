#include <iostream>
using namespace std;
int main() {
    char string[] = "nohtyp";
    int i,j;
    for (j = 0; string[j] != '\0'; j++);
    j = j-1;
    for(i = 0; i < j; i++, j--) {
        char temp = string[i];
        string[i] = string[j];
        string[j] = temp;
    }
    cout << string;
    return 0;
}
