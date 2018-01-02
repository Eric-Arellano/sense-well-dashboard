# Sense Well Dashboard
React & Flask app to visualize sensor data for clean water wells to detect when they fail prematurely.

## To install

### Requirements
1. Python 3.6
    1. Mac: use HomeBrew and `brew install python3`
    1. Windows: download at https://www.python.org/downloads/ 
        1. Check off the option to add python.exe to your PATH variable.
1. NVM (Node Version Manager)
    1. Mac: https://github.com/creationix/nvm/blob/master/README.md
    1. Windows: https://github.com/coreybutler/nvm-windows
1. Node.js (use NVM)
    1. `nvm install 9.3.0`
    1. `nvm use 9.3.0`
1. Yarn
    1. `npm install --global yarn`

#### Backend
1. `cd backend/`
1. Make a virtual environment:
    1. Mac: `python3 -m venv ./`
    1. Windows: `python -m venv ./`
1. `cd ../`
1. activate virtual environment:
    1. On Mac, `source backend/bin/activate`
    1. On Windows, `backend\Scripts\activate.bat`
1. install dependencies: `pip install -r requirements.txt`

#### Frontend
1. `cd frontend/`
1. `yarn install`

## To run

### Backend
`./run-backend.sh`

### Frontend
`./run-frontend.sh`

##### To build (rendered by backend)
`./run-frontend.sh build`

## To test

### Backend
`./run-backend.sh test`

##### To check type hints
`./run-backend.sh types`

##### To check type coverage
`./run-backend.sh coverage`

### Frontend

##### To check type hints
`./run-frontend.sh types`

## Dependency management

### Backend

##### See out of date dependencies
`pip list --outdated --format=columns`

##### Dependency tree
`pipdeptree`

##### Upgrade dependency
`pip install --upgrade <name>`

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