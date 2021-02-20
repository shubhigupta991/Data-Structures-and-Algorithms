#include <iostream>
using namespace std;

int main()
{
    char string[] = "How are you";
    int words = 1;
    for(int i = 0; string[i] != '\0'; i++) {
        if (string[i] == ' ' && string[i-1] != ' ')
            words ++;
    }
    cout << words;
    return 0;
}
