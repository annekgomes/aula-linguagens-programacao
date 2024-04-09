#include <iostream>

using namespace std;

int main() {

    string nome;
    string sobrenome;

    cin >> nome;
    cin >> sobrenome;

    int ult_posi = nome.length() -1;

    cout << sobrenome << nome[0] << "," << nome[ult_posi] << endl;

    return 0;
}