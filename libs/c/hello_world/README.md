https://pgi-jcns.fz-juelich.de/portal/pages/using-c-from-python.html

https://stackoverflow.com/questions/16647186/calling-c-functions-in-python


https://askubuntu.com/questions/931940/unable-to-change-the-root-password-in-windows-10-wsl


```
wsl -u root
passwd devcontainers
```


sudo apt install g++
g++ --version

https://pgi-jcns.fz-juelich.de/portal/pages/using-c-from-python.html

cc -fPIC -shared -o libsum.so sum.c

g++ main.c


g++ (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0

# windows setup c
https://code.visualstudio.com/docs/languages/cpp#_set-up-your-c-environment


There is the suggestion to use wsl and yeah probably just use that to get started?

But I think that also means running pygame on wsl??

https://learn.microsoft.com/en-us/windows/wsl/install


visual studio 2026 community edition is probably the easiest way to get the c++ compilers for windows specifically.

c/c++ is pretty low level and so there isn't a strong guarantee that the libraries I'm borrowing will even work on both linux and windows.




```
wsl --install
wsl --update
```

reboot windows

wsl.exe is started up and Ubuntu is installed by default so nothing else should be required


https://ubuntu.com/desktop/wsl


I still ended up installing when prompted on vscode


 C:\Windows\System32\wsl.exe --install -d Ubuntu-20.04


  g++ --version
Command 'g++' not found, but can be installed with:
sudo apt install g++


I think once wsl is setup I'm just following the ubuntu instructions?

Let me check pygame.


The window does look a little different. I am running a emulation of ubuntu.

Pretty big degredation running pygame through wsl on windows.


So doing some testing in wsl for my sound library is probably okay but I will want to switch back to windows.

Visual studio installer