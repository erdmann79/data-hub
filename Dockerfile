# base image  
FROM python:3.9.7 as base

# set environment variables  
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.15

RUN pip install --upgrade pip

RUN pip install 'poetry=='$POETRY_VERSION

COPY poetry.lock pyproject.toml /app/
COPY . . /app/

WORKDIR /app
#RUN poetry config virtualenvs.create false --local
RUN poetry config virtualenvs.in-project true --local

RUN poetry install --no-interaction --no-root --no-dev


FROM python:3.9.7-slim as runtime
ARG SECRET_KEY_ARG
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    SECRET_KEY=$SECRET_KEY_ARG
WORKDIR /app
ENV PATH=/app/.venv/bin:$PATH
COPY --from=base /app/.venv /app/.venv
COPY --from=base /app/ /app/

#ENV LANG en_US.utf8
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

