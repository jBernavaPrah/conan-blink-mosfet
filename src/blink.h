#pragma once

#ifdef WIN32
  #define blink_EXPORT __declspec(dllexport)
#else
  #define blink_EXPORT
#endif

blink_EXPORT void blink();
