#include <termios.h>
#include <iostream>
#include <bitset>


using namespace std;

int main() {
    struct termios tty;
    std::cout << bitset<32>(tty.c_cflag) << endl;
    std::cout << bitset<8>(CS8) << endl;
    return 0;
}
