
# static struct PyModuleDef pysimple_module = {PyModuleDef_HEAD_INIT, "_core",
                                            #  NULL, -1, pysimple_methods};
# from vgmplay._core import *
from vgmplay._module import square

# from ._core import *

# from ._module import square

__all__ = [square]


# __all__ = [hello_from_bin]