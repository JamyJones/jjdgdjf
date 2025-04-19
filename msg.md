I have  problem on my ci i know i can solve it by updating my docker image but i  don't want to
when i run 'apt install update'  the script fails due to No_PUBKEY. This is the log output
Each error is as follows. So i want to grab the key-id and then add it to "sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys key-id" command and then run the 'apt install update' again. In a script
Ign:1 http://archive.ubuntu.com/ubuntu disco InRelease
 Ign:2 http://archive.ubuntu.com/ubuntu disco-updates InRelease
 Ign:3 http://archive.ubuntu.com/ubuntu disco-backports InRelease
 Err:4 http://archive.ubuntu.com/ubuntu disco Release
   404  Not Found [IP: 91.189.91.83 80]
 Err:5 http://archive.ubuntu.com/ubuntu disco-updates Release
   404  Not Found [IP: 91.189.91.83 80]
 Err:6 http://archive.ubuntu.com/ubuntu disco-backports Release
   404  Not Found [IP: 91.189.91.83 80]                            Ign:7 http://security.ubuntu.com/ubuntu disco-security InRelease
 Err:8 http://security.ubuntu.com/ubuntu disco-security Release
   404  Not Found [IP: 91.189.91.82 80]                            Get:9 https://apt.llvm.org/noble llvm-toolchain-noble-18 InRelease [5554 B]
 Err:9 https://apt.llvm.org/noble llvm-toolchain-noble-18 InRelease
   The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 15CF4D18AF4F7421