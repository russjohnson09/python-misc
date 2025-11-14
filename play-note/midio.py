# https://github.com/mido/mido

import mido

# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# ModuleNotFoundError: No module named 'rtmidi'
# supports RtMidi, PortMidi and Pygame. New backends are easy to write.

# uv add rtmidi

    #   copying rtmidi\collector.py -> build\lib.win-amd64-cpython-313\rtmidi
    #   copying rtmidi\randomout.py -> build\lib.win-amd64-cpython-313\rtmidi
    #   copying rtmidi\__init__.py -> build\lib.win-amd64-cpython-313\rtmidi
    #   running build_ext
    #   building 'rtmidi._rtmidi' extension

    #   [stderr]
    #   C:\Users\russj\AppData\Local\uv\cache\builds-v0\.tmpD4bDiN\Lib\site-packages\setuptools\_distutils\extension.py:150: UserWarning: Unknown Extension options: 'headers'
    #     warnings.warn(msg)
    #   C:\Users\russj\AppData\Local\uv\cache\builds-v0\.tmpD4bDiN\Lib\site-packages\setuptools\_distutils\dist.py:289: UserWarning: Unknown distribution option:
    #   'description_content_type'
    #     warnings.warn(msg)
    #   error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

port = mido.open_output('Port Name')

mid = mido.MidiFile('twinkle-twinkle-little-star.mid')
for msg in mid.play():
    port.send(msg)