#include <iostream>
#include <fstream>

using namespace std;

int main () {
    ifstream inFile;
    inFile.open("../day2.txt");
    if (inFile.is_open()) {
        while (!inFile.eof()) {
            inFile >> output;
            cout << output;
        }
    };
    inFile.close()
    cout << "lmao bruh";
    return 0;
};