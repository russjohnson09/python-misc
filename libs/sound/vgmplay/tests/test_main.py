import vgmplay



#  uv run pytest -s
def test_main():

    assert 1 == 1

    print(vgmplay)

    assert vgmplay.square(3) == 9

    # assert vgmplay.hello_from_bin() == 'Hello from vgmplay!'