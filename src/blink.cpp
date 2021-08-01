#include <iostream>
#include "blink.h"
#include "pico/stdlib.h"

void blink(){
    #ifdef NDEBUG
    std::cout << "blink/0.1: Hello World Release!" <<std::endl;
    #else
    std::cout << "blink/0.1: Hello World Debug!" <<std::endl;
    #endif
}
