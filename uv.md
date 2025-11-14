https://docs.astral.sh/uv/getting-started/installation/

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


PS C:\Users\russj> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Downloading uv 0.9.9 (x86_64-pc-windows-msvc)
Installing to C:\Users\russj\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
everything's installed!

To add C:\Users\russj\.local\bin to your PATH, either restart your shell or run:

    set Path=C:\Users\russj\.local\bin;%Path%   (cmd)
    $env:Path = "C:\Users\russj\.local\bin;$env:Path"   (powershell)





uv init --lib lib-models