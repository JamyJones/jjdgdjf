I want the object code *.o but i don't know how to modify this make file
TERMUX_PREFIX := /data/data/com.termux/files/usr
TERMUX_BASE_DIR := /data/data/com.termux/files
CFLAGS += -Wall -Wextra -Werror -fPIC
#for fpdfium
#-lpdfium
# Rule to create the shared library
libbackport.a: main.cpp
        $(CXX) -I$(TERMUX_PREFIX)/include -c main.c -o libbackport.o

install: libbackport.o
        install libbackport.a $(DESTDIR)$(PREFIX)/lib/libbackport.a

uninstall:
        rm -f $(DESTDIR)$(PREFIX)/lib/libbackport.a