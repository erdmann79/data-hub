# base image  
FROM python:3.9.7 as base

# setup environment variables
# ENV PYTHONFAULTHANDLER=1 \
#     PYTHONHASHSEED=random \
#     PYTHONUNBUFFERED=1 \
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
    #DockerHOME=/home/app/webapp  

## set work directory  
#RUN mkdir -p $DockerHOME  
#
## where your code lives  
#WORKDIR $DockerHOME  

WORKDIR /app

FROM base as builder

# set more environment variables  
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.5



FROM base as poetry
RUN pip install poetry==1.1.15
COPY poetry.lock pyproject.toml /app/
RUN poetry export -o requirements.txt
RUN pip-compile --generate-hashes -o requirements.txt requirements.txt


FROM base as build
COPY --from=poetry /app/requirements.txt /tmp/requirements.txt
RUN python -m venv .venv && \
    .venv/bin/pip install 'wheel==0.36.2' && \
    .venv/bin/pip install -r /tmp/requirements.txt



#RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
RUN pip install "poetry==$POETRY_VERSION"
#RUN python -m venv /venv



FROM python:3.9.7-slim as runtime
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
ENV PATH=/app/.venv/bin:$PATH
COPY --from=build /app/.venv /app/.venv
COPY . /app

CMD ["manage.py", "runserver"]



#RUN poetry install --no-interaction --no-root
#
#CMD ["poetry", "run", "manage.py", "runserver"]

#
## install dependencies  
#RUN pip install --upgrade pip  
#
#RUN pip install 'poetry==$POETRY_VERSION'
#
## copy whole project to your docker home directory. 
#COPY . $DockerHOME  
## run this command to install all dependencies  
#
#RUN poetry install --no-interaction --no-root
#
## port where the Django app runs  
#EXPOSE 8000  
## start server  
#CMD python manage.py runserver 
#
#





#FROM python:3.7.6-alpine3.11 as base
#
#ENV PYTHONFAULTHANDLER=1 \
#    PYTHONHASHSEED=random \
#    PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#FROM base as builder
#
#ENV PIP_DEFAULT_TIMEOUT=100 \
#    PIP_DISABLE_PIP_VERSION_CHECK=1 \
#    PIP_NO_CACHE_DIR=1 \
#    POETRY_VERSION=1.0.5
#
#RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
#RUN pip install "poetry==$POETRY_VERSION"
#RUN python -m venv /venv
#
#COPY pyproject.toml poetry.lock ./
#RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin
#
#COPY . .
#RUN poetry build && /venv/bin/pip install dist/*.whl
#
#FROM base as final
#
#RUN apk add --no-cache libffi libpq
#COPY --from=builder /venv /venv
#COPY docker-entrypoint.sh wsgi.py ./
#CMD ["./docker-entrypoint.sh"]#