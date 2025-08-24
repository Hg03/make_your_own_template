FROM python:3.10-slim-bookworm

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        git \
        unzip \
        curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

# Install uv and run sync in the same command
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    /root/.local/bin/uv sync

ENV PATH="/root/.local/bin:$PATH"
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE $PORT

CMD ["streamlit", "run", "src/myot/app.py"]