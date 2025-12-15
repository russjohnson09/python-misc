https://stackoverflow.com/questions/56309251/what-is-the-meaning-of-building-wheel-for-xxx-when-i-use-pip-install-package



https://pythonwheels.com/


https://docs.astral.sh/uv/reference/settings/#package


https://sgoel.dev/posts/building-cython-or-c-extensions-using-uv/


https://github.com/scikit-build/scikit-build-core


https://setuptools.pypa.io/en/latest/userguide/ext_modules.html

https://setuptools.pypa.io/en/latest/userguide/quickstart.html


Community\VC\Tools\MSVC\14.50.35717\lib\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\lib\um\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.26100.0\ucrt\x64" "/LIBPATH:C:\Program Files (x86)\Windows Kits\10\\lib\10.0.26100.0\\um\x64" /EXPORT:PyInit_add build\temp.win-amd64-cpython-313\Release\add.obj /OUT:build\lib.win-amd64-cpython-313\add.cp313-win_amd64.pyd /IMPLIB:build\temp.win-amd64-cpython-313\Release\add.cp313-win_amd64.lib
LINK : error LNK2001: unresolved external symbol PyInit_add
build\temp.win-amd64-cpython-313\Release\add.cp313-win_amd64.lib : fatal error LNK1120: 1 unresolved externals
error: command 'C:\\Program Files\\Microsoft Visual Studio\\18\\Community\\VC\\Tools\\MSVC\\14.50.35717\\bin\\HostX86\\x64\\link.exe' failed with exit code 1120
  × Failed to build `C:\Users\russj\dev\python-misc\libs\lib-add`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit code: 1)