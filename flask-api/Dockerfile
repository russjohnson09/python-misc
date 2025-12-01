# syntax=docker/dockerfile:1
# FROM python:3.13-slim AS build
# TODO git should only be required for the build
FROM python:3.13 AS build

WORKDIR /app

# RUN apt-get install git

# Install uv (alternative: copy from ghcr.io/astral-sh/uv:0.x.x)
RUN pip install uv

# COPY uv.lock pyproject.toml ./
# RUN uv sync --no-install-project --no-dev

COPY . .
# RUN uv sync --no-install-project --no-dev
RUN uv sync --no-dev


CMD ["sh", "/app/start.sh"]


# WORKDIR /app
# ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy



# FROM python:3.13-slim AS runtime
# ENV PATH="/app/.venv/bin:$PATH" # Adjust if not using a venv

# RUN groupadd -g 1001 appgroup && \
#     useradd -u 1001 -g appgroup -m -d /app -s /bin/false appuser

# WORKDIR /app
# COPY --from=build --chown=appuser:appgroup /app .

# CMD ["python", "your_app.py"]


        # command: gunicorn --bind 0.0.0.0:8080 --log-level info app:app
