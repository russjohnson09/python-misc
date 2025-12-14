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

WORKDIR /app



# docker build .
# TODO proper multipar build
# https://docs.docker.com/build/building/multi-stage/
#  As builder
# ERROR: failed to solve: failed to parse stage name "BASE": invalid reference format: repository name (library/BASE) must be lowercase
# lowercase does matter here
FROM base AS build

# https://docs.docker.com/reference/dockerfile/#workdir
WORKDIR /app

# is setting the working directory necessary

# https://hub.docker.com/_/python


# FROM ubuntu:22.04

# https://github.com/docker-library/python/blob/3f2d7e4c339ab883455b81a873519f1d0f2cd80a/3.13/alpine3.22/Dockerfile


# https://github.com/astral-sh/uv/issues/6392

RUN pwd


# https://pkgs.alpinelinux.org/package/edge/main/x86_64/build-base
## cc compiler
RUN apk add curl git uv build-base

COPY ./pyproject.toml pyproject.toml
# COPY ./uv.lock uv.lock

# https://mathspp.com/blog/uv-cheatsheet
RUN uv venv

# The libraries themselves could be built if I had pkgconfig?
# 6.803       Run-time dependency sdl2 found: NO (tried pkgconfig, config-tool and
# RUN apk add sdl2 sdl2_image sdl2_image-dev sdl2_mixer sdl2_mixer-dev
# # 6.967       Library SDL2 found: YES
# # 6.967       Run-time dependency sdl2_image found: NO (tried pkgconfig and cmake)
# RUN apk add sdl2_ttf sdl2_ttf-dev

# 6.761       Did not find CMake 'cmake'
# portmidi
# enable building the above
# https://pkgs.alpinelinux.org/package/edge/main/x86/pkgconf
# https://pkgs.alpinelinux.org/package/edge/main/x86/cmake


# RUN apk add ninja
# RUN apk add meson 



# RUN apk add libasound2-dev

#/tmp/portmidi
# RUN git clone https://github.com/PortMidi/portmidi.git /tmp/portmidi && cd /tmp/portmidi && cmake . && make && make install

# https://pypi.org/project/pygame-ce/
# https://docs.astral.sh/uv/concepts/projects/sync/#partial-installations
RUN uv sync --all-extras --no-install-project

COPY ./ .

RUN uv sync --all-extras


# docker build . --target=run --progress plain -t lib-sounds-test
# docker images
FROM base AS run
WORKDIR /app

# do I need to copy over portmidi again?
# do I reinstall 
COPY --from=build /app /app
# COPY ./ .

RUN ls /app/tests
RUN ls /app/tests/assets


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
#29 0.265 null
#29 0.265     Discard all samples (playback) or generate zero samples (capture)

# ALSA: Couldn't open aud
# os.environ['SDL_AUDIODRIVER'] = 'dsp'
# 1.309 ERROR tests/test_sounds.py::test_main - pygame.error: dsp: No such audio device
# ENV SDL_AUDIODRIVER='dsp' 

# #32 1.486 error: XDG_RUNTIME_DIR is invalid or not set in the environment.
# #31 1.535 ALSA lib conf.c:5205:(_snd_config_evaluate) function snd_func_card_inum returned error: No such file or directory
# ENV SDL_AUDIODRIVER='alsa' 
ENV SDL_AUDIODRIVER='dummy' 

RUN ls /app/tests/assets
RUN uv sync --all-extras
RUN ls /app/tests/assets

ENV ASSET_DIR='/app/tests/assets' 

# #37 12.67 tests/test_main.py Fatal Python error: Segmentation fault
# only main has the segmentation fault though
# RUN uv run pytest