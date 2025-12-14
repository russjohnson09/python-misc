import ctypes
import os



_root_repo_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../../'))
# full path from os
_sum = ctypes.CDLL('./libsum.so')
# _sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_default_lib_dir = os.path.abspath(os.path.join(_root_repo_dir, 'assets'))

os.environ['ASSET_DIR'] = _default_asset_dir

def main():
    print("Hello from hello-world!")


if __name__ == "__main__":
    main()
