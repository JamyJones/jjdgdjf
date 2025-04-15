What compiler flags can i pass in while using ndk to compile code for older api like i want to compile some code for 0android 6.0.1 , the compiler gives me errors about missing function fseeko,etc that were introduced in android 7.0+ .when i compile for say target api 24 the compiler successfully compiles but when i set api 23, the errors come up about missing symbols. I want to backport such functions functions but i don't know how
(I don't know if these are the only missing but if you know more please add them for me or provide a reference to where i can download from their definitions)
#if __ANDROID_API__ < 24
#include <stdio.h>
#include <sys/types.h>
long ftello(FILE *stream) {
    return ftell(stream);
}
int fseeko(FILE *stream, off_t offset, int whence) {
    return fseek(stream, (long)offset, whence);
}
#endif

This code could work but i don't know how to let the compiler know that i have defined these symbols here, for some reason i don't want modify the original source files(i don't want to do things like "#include...") because there's like a hundred files that use such symbols/functions . If only there's a way for the compiler to know that i did define these symbols in file. Am Prefer using a Makefile