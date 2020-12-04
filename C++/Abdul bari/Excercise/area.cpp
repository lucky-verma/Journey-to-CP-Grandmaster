#include <iostream>

using namespace std;

int main() {
    float radius, area;
    cout<< "Enter radius to find Area = ";
    cin>>radius;
    area = 3.14f * radius * radius;
    cout<<"The area of circle is "<<area; 
    return 0;
}