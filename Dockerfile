FROM python:3.13-alpine AS base

RUN apk add pkgconf cmake

# https://krython.com/post/installing-compilers-and-build-tools-in-alpine-linux/
RUN apk add clang clang-dev llvm llvm-dev
RUN apk add clang-extra-tools
RUN apk add cmake cmake-doc
RUN apk add extra-cmake-modules
RUN apk add openssl-dev

# install runtime dependencies only
RUN apk add curl git uv build-base
# https://github.com/PortMidi/portmidi
RUN apk add alsa-lib-dev
RUN git clone https://github.com/PortMidi/portmidi.git /tmp/portmidi && cd /tmp/portmidi && cmake . && make && make install

RUN apk add sdl2-dev sdl2_image-dev sdl2_ttf-dev sdl2_mixer sdl2_mixer-dev


# remove any non runtime packages used in previous steps
RUN apk del build-base clang clang-extra-tools extra-cmake-modules

RUN apk add alsa-utils
# RUN apk add libasound2
# https://www.reddit.com/r/AlpineLinux/comments/plf465/how_to_setup_audio_on_alpine/
# https://wiki.alpinelinux.org/wiki/ALSA
RUN apk add alsa-lib
RUN apk add alsaconf

# https://stackoverflow.com/questions/57882375/emulate-sound-card-alsa-snd-dummy-docker-kernel-rebuild-alsa-snd-dummy
# https://askubuntu.com/questions/1406646/ubuntu-22-04-audio-output-not-working-dummy-audio
RUN aplay -L
RUN aplay -L

ENV SDL_AUDIODRIVER='dummy' 

WORKDIR /app

COPY ./ .
# #22 0.045 /bin/sh: cd: line 0: can't cd to pygame/galaga: No such file or directory
RUN cd pygame/galaga && uv sync --all-extras