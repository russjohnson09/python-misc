import lib_add_c


def test_main():

    assert 1 == 1

    print(lib_add_c) #tests\test_main.py <module 'lib_add_c' from 'C:\\Users\\russj\\dev\\python-misc\\libs\\lib-add-c\\src\\lib_add_c\\__init__.py'>

    pass


def test_add():

    assert lib_add_c.add(1,1) == 2