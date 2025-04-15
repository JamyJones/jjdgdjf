What compiler flags can i pass in while using ndk to compile code for older api like i want to compile some code for 0android 6.0.1 , the compiler gives me errors about missing function fseeko,etc that were introduced in android 7.0+ .when i compile for say target api 24 the compiler successfully compiles but when i set api 23, the errors come up about missing symbols. I want to backport such functions functions but i don't know how (I don't know if these are the only missing but if you know more please add them for me or provide a reference to where i can download from their definitions) #if __ANDROID_API__ < 24 #include #include long ftello(FILE *stream) { return ftell(stream); } int fseeko(FILE *stream, off_t offset, int whence) { return fseek(stream, (long)offset, whence); } #endif This code could work but i don't know how to let the compiler know that i have defined these symbols here, for some reason i don't want modify the original source files(i don't want to do things like "#include...") because there's like a hundred files that use such symbols/functions . If only there's a way for the compiler to know that i did define these symbols in file. Actually the thing is the build system i have only allows access direct to the compiler via viriables like LDflags ,
source/fitz/output.c:150:10: error: call to undeclared function 'fseeko'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
   150 |         int n = fseeko(file, off, whence);
       |                 ^
 source/fitz/output.c:150:10: note: did you mean 'fseek'?
 /home/builder/.termux-build/_cache/android-r27c-api-23-v1/bin/../sysroot/usr/include/stdio.h:212:5: note: 'fseek' declared here
   212 | int fseek(FILE* _Nonnull __fp, long __offset, int __whence);
       |     ^
 source/fitz/output.c:163:16: error: call to undeclared function 'ftello'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
   163 |         int64_t off = ftello(file);                             |                       ^
 source/fitz/output.c:163:16: note: did you mean 'ftell'?
 /home/builder/.termux-build/_cache/android-r27c-api-23-v1/bin/../sysroot/usr/include/stdio.h:213:6: note: 'ftell' declared here
   213 | long ftell(FILE* _Nonnull __fp);
       |      ^
 source/fitz/output.c:200:15: error: call to undeclared function 'ftello'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
   200 |                 off_t pos = ftello(file);
       |                             ^
 3 errors generated.
 make: *** [Makefile:151: build/release/source/fitz/output.o] Error 1
 m