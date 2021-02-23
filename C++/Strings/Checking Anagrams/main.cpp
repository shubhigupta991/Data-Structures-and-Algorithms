#include <iostream>
using namespace std;

void anagram1(char *S, char *A) {
    int k = 0;
    for(int i = 0; S[i] != '\0'; i++) {
        for(int j = 0; A[j] != '\0'; j++) {
            if (S[i] == A[j])
                k = 1;
        }
        if (k == 0)
            cout << "Not Anagrams";
    }
    if (k == 1)
        cout << "Anagrams";
}
void anagram2(char *S, char *A) {
    int H[26] = {0};
    int k = 1;
    for(int i = 0; S[i] != '\0'; i++) {
        H[S[i] - 97] += 1;
    }
    for(int i = 0; A[i] != '\0'; i++) {
        H[A[i] - 97] -= 1;
        if (H[A[i] - 97] < 0) {
            cout << "Not Anagrams";
            k = 0;
        }
    }
    if (k == 1)
        cout << "Anagrams";
}
int main() {
    char *A = "decimal";
    char *B = "medical";
    anagram1(A,B);
    cout << endl;
    anagram2(A,B);
    return 0;
}
