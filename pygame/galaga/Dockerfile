# https://hub.docker.com/_/python
# FROM python:3.13-alpine
# https://hub.docker.com/r/astral/uv
# FROM ghcr.io/astral-sh/uv:python3.13-alpine
FROM astral-sh/uv:python3.13-alpine



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

RUN uv env
RUN uv sync --locked --all-extras
# RUN uv sync --locked --all-extras --dev

# TODO CMD startup