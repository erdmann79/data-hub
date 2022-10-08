# data-hub
Django/Mongodb 

## The problem
the problem

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
  <img src="./images/IMG_20220812_221020_01.jpg" align="top" alt="Breadboard1" width="350">
  <img src="./images/IMG_20220815_171640_01.jpg" align="top" alt="Breadboard2" width="350">
</p>
<p float="left">
  <img src="./images/Screenshot_20220816-222419.png" align="top" alt="HASS phone app" width="350">
  <img src="/images/Screenshot from 2022-08-29 18-51-03.png" align="top" alt="HASS Web Panel" width="350">
</p>

