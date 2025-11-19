# https://hub.docker.com/_/python
# FROM python:3.13-alpine
# FROM ghcr.io/astral-sh/uv:python3.13-alpine
# https://hub.docker.com/r/astral/uv
# FROM astral/uv:python3.13-alpine
FROM python:3.13-alpine AS run


RUN apk add curl git uv build-base
# RUN apk add curl git build-base

# FROM ubuntu:22.04

# https://github.com/docker-library/python/blob/3f2d7e4c339ab883455b81a873519f1d0f2cd80a/3.13/alpine3.22/Dockerfile


# https://github.com/astral-sh/uv/issues/6392

# RUN apk add --no-cache curl git

# # RUN curl -LsSf -o /tmp/install_uv.sh https://astral.sh/uv/install.sh && \
# #     sh /tmp/install_uv.sh && \
# #     rm /tmp/install_uv.sh
# ENV PATH="/root/.local/bin:$PATH"
# # 

# RUN apk add uv

COPY ./.python-version .python-version
COPY ./pyproject.toml pyproject.toml
COPY ./uv.lock uv.lock

RUN uv venv
# https://docs.astral.sh/uv/concepts/projects/sync/#partial-installations
RUN uv sync --all-extras --no-install-project

COPY ./ .

RUN uv sync --locked --all-extras
# RUN uv sync --locked --all-extras --dev

# TODO CMD startup