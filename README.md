# data-hub
Django/Mongodb 

## The problem
Pipeline work

## Repository Build

### Python setup
For your convenience, setting up the virtual environment has been automated using poetry. https://python-poetry.org/ You must have python with poetry installed.

### Install Poetry
```bash
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
````
Feel free to look here for more instructions. Updating Poetry is very easy by the way ```poetry update```.

### Install the virtual environment
Navigate to the root directory of the project and run "poetry install"
```bash
~/projects/data-hub$ poetry install
````

### Interactive Shell
Switch to the interactive enviroment (PYTHON) by typing "poetry shell". Note the environment, the python activation, and path your the virtual environment, as well as the change to the prompt to include the current python shell and version.

```bash
$ poetry shell
~/projects/roster$ . /home/<username>/.cache/pypoetry/virtualenvs/data-hub-JxgitZP8-py3.10/bin/activate
(data-hub-JxgitZP8-py3.10) $~/projects/data-hub$
````

## Docker Deploy from dockerhub

### Install Docker
Install Docker

### Docker-hub
```bash
$ poetry shell
~/projects/roster$ docker pull erdmann79/data-hub
````

## Pictures
<p float="left">
  <img src="./images/b86bd0a4-2c55-4935-b3a4-f865384e7800.png" align="top" alt="Breadboard1" width="350">
</p>

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: data-hub
spec:
  selector:
    matchLabels:
      app: data-hub
  replicas: 1
  template:
    metadata:
      labels:
        app: data-hub
    spec:
      containers:
      - name: data-hub
        imagePullPolicy: Always
        image: erdmann79/data-hub
        ports:
        - containerPort: 8000
---
