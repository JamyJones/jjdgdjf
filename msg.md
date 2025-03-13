nm -D libc.so | grep __aeabi_memcpy
After running the command above i get two outputs

000175d6 W __aeabi_memcpy
000175d6 W __aeabi_memcpy4
000175d6 W __aeabi_memcpy8

The other output is
0000cabe T __aeabi_memcpy
0000cac0 T __aeabi_memcpy4
0000cac2 T __aeabi_memcpy8