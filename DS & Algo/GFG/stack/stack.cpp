#include <iostream>
using namespace std;
int stack[100], top = -1, n = 100;
void push(int x)
{
    if (top >= n - 1)
    {
        cout << "Stack OverFlow";
    }
    else
    {
        stack[++top] = x;
    }
}
void pop()
{
    stack[--top];
}
void peek()
{  
    cout<<stack[top]<<endl;
}
void display()
{
    if (top >= 0)
    {
        for (int i = top; i >= 0; i--)
        {
            cout << stack[i] << endl;
        }
    }
}
int main()
{
    int value, ch;
    // cout << "Enter the Stack Values to be inserted";
    cout << "\n 1) Push \n 2)Pop \n 3) Peek \n 4)Display Stack \n";
    cout << "Enter the case";
    ch = 0;
    while (ch != 10)
    {
        cout << "Enter the case value:  ";

        cin >> ch;
        switch (ch)
        {
        case 1:
        {
            //Push operation
            cout << "Enter the value to be pushed";
            cin >> value;
            push(value);
            break;
        }
        case 2:
        {
            //Pop Operation
            pop();
            break;
        }
        case 3:
        {
            //Peek Operation
            peek();
            break;
        }
        case 4:
        {
            display();
        }
        }
    }
    return 0;
}