import os
import vgmplay



#  uv run pytest -s
def test_main():

    assert 1 == 1

    # E   ImportError: /mnt/c/Users/russj/dev/python-misc/libs/sound/vgmplay/.venv/lib/python3.13/site-packages/vgmplay/_module.cpython-313-x86_64-linux-gnu.so: undefined symbol: gzclose
    print(vgmplay)

    assert vgmplay.square(3) == 9
    assert vgmplay.square_int(3) == 9

    result = vgmplay.echo('test')

    assert str(type(result)) == "<class 'bytes'>"
    assert type(result) is bytes

    print(result.decode('utf-8'))

    assert result.decode('utf-8') == 'test'

# https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple
    result = vgmplay.echo2('test', 'test2')

    assert result.decode('utf-8') == 'test2'

    dir = os.path.dirname(__file__)
    print(dir)

    vgm_file = os.path.abspath(os.path.join(dir, 'nakama.vgm'))
    vgm_wav = os.path.abspath(os.path.join(dir, 'nakama.wav'))

    print(vgm_file, vgm_wav)


    vgmplay.vgm2wav(vgm_file, vgm_wav)


    # assert vgmplay.hello_from_bin() == 'Hello from vgmplay!'