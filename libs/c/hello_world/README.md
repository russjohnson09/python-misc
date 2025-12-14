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