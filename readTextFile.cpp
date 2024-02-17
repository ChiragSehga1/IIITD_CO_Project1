#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<string> readTextFile(){
    /*reads instructions.txt and returns a vector.
    Each element on the vector is a different instruction line */
    vector<string> instructions;
    ifstream file("instructions.txt");
    string i;
    while (getline(file, i)){
        instructions.push_back(i);
    }
    file.close();
    return instructions;
}

int main(){
    vector<string> g1;
    g1=readTextFile();
    for (auto i = g1.begin(); i != g1.end(); ++i)
        cout << *i << endl;
    return 0;
}