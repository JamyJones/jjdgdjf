what is the error in my bash script
#!/bin/bash

muBuild(){
curl -L "https://github.com/ArtifexSoftware/mupdf/archive/refs/tags/1.25.6.zip" -o mu.zip
unzip mu.zip -d mu
cd mu/mupdf-1.25.6
export TOOLCHAIN=/usr/local/lib/android/sdk/ndk/27.2.12479018/toolchains/llvm/prebuilt/linux-x86_64/bin
export CC=$TOOLCHAIN/armv7a-linux-androideabi23-clang
export CXX=$TOOLCHAIN/armv7a-linux-androideabi23-clang++
sudo make CC=$CC CXX="$CXX" prefix='/usr/local' HAVE_X11=no tesseract=no shared=no build=release HAVE_GLUT=no HAVE_OBJCOPY=no USE_SYSTEM_GLUT=no install