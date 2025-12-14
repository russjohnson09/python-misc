https://askubuntu.com/questions/1128112/ld-cannot-find-shared-library


g++ -o prog main.o -L. -lsum


ld -L. -lsum --verbose

ld -Llib -lsum --verbose

g++ -o prog main.o -Llib -lsum

ldd ./prog
        linux-vdso.so.1 (0x00007ffc500d2000)
        libsum.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f54a2daa000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f54a2fc9000)


https://unix.stackexchange.com/questions/451544/g-cant-find-so-files-in-usr-local-lib-even-when-added-to-etc-ld-so-conf


https://stackoverflow.com/questions/10749058/building-and-linking-a-shared-library

g++ -o checkbeat checkbeat.cpp -I . -L. libbeat.so.1.0.1


g++ -o prog main.c -I. -L. -lsum



 g++ -o prog main.c -I . -L. ./libsum.so