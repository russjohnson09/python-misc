import ctypes
import os



_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
# full path from os
_default_lib_dir = os.path.abspath(os.path.join(_root_repo_dir, 'libs/c/hello_world/libsum.so'))

libsum_so_path = os.environ.get('RUSS_LIBSUM_PATH', _default_lib_dir)

_sum = ctypes.CDLL(libsum_so_path)#)'./libsum.so')

# AttributeError: function 'our_function' not found
# _sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# <CDLL 'C:\Users\russj\dev\python-misc\libs\c\hello_world\libsum.so', handle 7fff64780000 at 0x1fc9e587a10>
print(_sum)
_sum.add.argtypes = (ctypes.c_int, ctypes.c_int)

# https://stackoverflow.com/questions/5311515/gcc-fpic-option

# g++ -shared -o libsum.so sum.cpp
def main():
    print("Hello from hello-world!")

    sum_result = _sum.add(1,1)
    print(sum_result) # 2


if __name__ == "__main__":
    main()
