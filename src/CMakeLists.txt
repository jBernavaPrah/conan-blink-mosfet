cmake_minimum_required(VERSION 3.19)


include(../../pico_sdk_import.cmake)
project(blink C CXX ASM)
pico_sdk_init()

add_library(blink blink.cpp)

# Pull in our pico_stdlib which pulls in commonly used features
target_link_libraries(blink pico_stdlib ${CONAN_LIBS})

add_compile_options(-Wall
        -Wno-format          # int != int32_t as far as the compiler is concerned because gcc has int32_t as long int
        -Wno-unused-function # we have some for the docs that aren't called
        -Wno-maybe-uninitialized
        )


# enable usb output, disable uart output
pico_enable_stdio_usb(blink 1)
pico_enable_stdio_uart(blink 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(blink)

