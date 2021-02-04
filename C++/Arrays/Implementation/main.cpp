#include <iostream>
using namespace std;

class Array {
private:
    int *A;
    int size;
    int length;

public:
    Array() {
        size = 10;
        length = 0;
        A = new int[size];
    }

    Array(int s) {
        size = s;
        length = 0;
        A = new int[size];
    }

    void Display() {
        cout << "Elements of array are : " << endl;
        for(int i = 0; i < length; i++) {
            cout << A[i] << '\t';
        }
    }

    void Append(int x) {
        if (length < size)
            A[length++] = x;
    }

    void Insert(int index, int x) {
        for(int i = length; i > index; i++)
            A[i] = A[i-1];
        A[index] = x;
        length++;
    }

    void Delete(int index) {
        for(int i = index; i < length; i++)
            A[i] = A[i+1];
        length--;
    }

    int LinearSearch(int key) {
        for(int i = 0; i < length; i++)
            if (A[i] == key)
                return i;
        return -1;
    }

    int BinarySearch(int key) {
        int beg = 0;
        int end = length;
        while (beg < end) {
            int mid = (beg + end) / 2;
            if (key == A[mid])
                return mid;
            else if (key < A[mid])
                end = mid - 1;
            else
                beg = mid + 1;
        }
        return -1;
    }

    int Get(int index){
        if (index >= 0 && index <= length)
            return A[index];
        return -1;
    }

    void Set(int index, int x) {
        if (index >= 0 && index <= length)
            A[index] = x;
    }

    int Max(){
        int max = A[0];
        for(int i = 0; i<length; i++) {
            if (A[i] > max)
                max = A[i];
        }
        return max;
    }

    int Min() {
        int min = A[0];
        for(int i = 0; i<length; i++) {
            if (A[i] < min)
                min = A[i];
        }
        return min;
    }

    int Sum() {
        int sum = 0;
        for(int i = 0; i < length; i++)
            sum += A[i];
        return sum;
    }

    float Avg() {
        return (float) Sum()/length;
    }

    void Reverse() {
        int *B;
        int i,j;
        B = (int*)malloc(length*sizeof(int));
        for(i = length - 1, j = 0; i >= 0; i--,j++)
            B[j] = A[i];

        for(i = 0; i < length; i++)
            A[i] = B[i];
    }

    void Reverse2() {
        int i,j;
        for(i = 0, j = length - 1; j >= 0; j--,i++)
            A[i] = A[j];
    }

    void InsertSort(int x) {
        int i = length-1;
        if( length== size)
            return;
        while(i>=0 &&  A[i]>x)
        {
            A[i+1]= A[i];
            i--;
        }
        A[i+1]=x;
        length++;
    }

    int isSorted() {
        for(int i = 0; i < length; i++){
            if (A[i] > A[i+1])
                return 0;
        }
        return 1;
    }

    Array * Merge(Array arr2) {
        int i,j,k;
        i = j = k = 0;

        Array *arr3 = new Array(length + arr2.length);
        while (i < length && j < arr2.length) {
            if(A[i]<arr2.A[j])
                arr3->A[k++]=A[i++];
            else
                arr3->A[k++]=arr2.A[j++];
        }

        for(;i<length;i++)
            arr3->A[k++]=A[i];
        for(;j<arr2.length;j++)
            arr3->A[k++]=arr2.A[j];

        arr3->length = k;
        return arr3;
    }

    Array * Union(Array arr2) {
        int i,j,k;
        i = j = k = 0;

        Array *arr3 = new Array();
        while (i < length && j < arr2.length) {
            if(A[i] < arr2.A[j])
                arr3->A[k++] = A[i++];
            else if(A[i] > arr2.A[j])
                arr3->A[k++] = arr2.A[j++];
            else {
                arr3->A[k++] = A[i++];
                j++;
            }

            for(;i<length;i++)
                arr3->A[k++]=A[i];
            for(;j<arr2.length;j++)
                arr3->A[k++]=arr2.A[j];

            arr3->length = k;
            return arr3;
        }
    }

    Array * Intersection(Array arr2) {
        int i, j, k;
        i = j = k = 0;

        Array *arr3 = new Array();
        if (A[i] == arr2.A[j]) {
            arr3->A[k++] = arr3->A[i++];
            j++;
        }

        arr3->length = k;
        return arr3;
    }

    Array * Diff(Array arr2) {
        int i, j, k;
        i = j = k = 0;

        Array *arr3 = new Array();
        if (A[i] == arr2.A[j])
            j++;
        else {
            arr3->A[k++] = A[i++];
            j++;
        }
    }

};


int main() {
    Array arr1;

    arr1.Append(1);
    arr1.Append(5);
    arr1.Insert(1,3);
    arr1.Display();
    arr1.Reverse();
    arr1.Display();
    cout << "Hello";
    return 0;
}
