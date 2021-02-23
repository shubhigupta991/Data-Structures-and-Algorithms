#include <iostream>
using namespace std;

void duplicates1(char *S) {
    for(int i = 0; S[i] != '\0'; i++) {
        for(int j = i+1; S[j] != '\0'; j++){
            if (S[i] == S[j])
                cout << S[i] << '\t';
        }
    }
}
void duplicates2(char *S) {
    int H[26] = {0};
    for(int i = 0; S[i] != '\0'; i++)
        H[S[i] - 97] += 1;

    for(int i = 0; i < 26; i++) {
        if (H[i] > 1)
            cout << char(i+97) << " = " << H[i] <<'\t';
    }
}
void duplicates3(char *S) {
    long int H = 0, x = 0;
    for(int i = 0; S[i] != '\0'; i++) {
        x = 1;
        x = x << S[i] - 97;

        if ((x & H) > 0)
            cout << S[i] << '\t';
        else
            H = x | H;
    }
}
int main() {
    char string[] = "finding";
    duplicates1(string);
    cout << endl;
    duplicates2(string);
    cout << endl;
    duplicates3(string);
    return 0;
}
