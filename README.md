# Sense Well Dashboard
React app to visualize sensor data for clean water wells to detect when they fail prematurely.

## To install

### Requirements
1. Python 3.6
    1. With Mac, use HomeBrew and `brew install python3`
1. NVM (Node Version Manager)
1. Node.js (use NVM)
    1. `nvm install 8.1.4`
    1. `nvm use 8.1.4`
1. Yarn
    1. `npm install --global yarn`

#### Backend
1. `cd backend/`
1. Make a virtual environment
    1. On Mac, `python3 -m venv ./`
    1. On Windows, `c:\Python35\python -m venv ./`
1. `cd ../`
1. activate virtual environment
    1. On Mac, `source backend/bin/activate`
    1. On Windows, `backend\Scripts\activate.bat`
1. `pip install -r requirements.txt`

#### Frontend
1. `cd frontend/`
1. `yarn install`
1. `yarn build`

## To run

### Backend
1. `./run-backend.sh`

### Frontend
1. `./run-frontend.sh`

##### To build (rendered by backend)
1. `./run-frontend.sh build`

## To test

### Backend
1. `./run-backend.sh test`

##### To check type hints
1. `./run-backend.sh types`

##### To check type coverage
1. `./run-backend.sh coverage`

### Frontend

##### To check type hints
1. `./run-frontend.sh types`

## Dependency management

##### See out of date dependencies
`pip list --outdated --format=columns`

##### Dependency tree
`pipdeptree`

##### Upgrade dependency
1. `pip install --upgrade <name>`

##### Update requirements.txt
1. Before making any changes, first delete everything with `pip freeze | xargs pip uninstall -y`. This is to make sure
there aren't outdated dependencies that you might inadvertently add.
1. `pip install -r requirements.txt`
1. Make whatever upgrades you want
1. `pip freeze > requirements.txt`

### Frontend
1. To add a new package:
    1. `cd frontend/`
    1. `yarn add <x>`
1. To remove a package:
    1. `cd frontend/`
    1. `yarn remove <x>`