#include <iostream>
#include <stdio.h>

class Array
{
    private:
    int length;
    int arr[100];
    int currLength;

    public:
    Array(int l)
    {
        int length = l;
        int arr[length];
        int currLength = 0;
    }

    void push(int value)
    {
        arr[currLength] = value;
        currLength++;
    }

    int pop()
    {
        
    }
}
