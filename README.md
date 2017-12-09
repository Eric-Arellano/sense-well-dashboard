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

## To start

#### Backend
1. activate virtual environment
    1. On Mac, `source backend/bin/activate`
    1. On Windows, `backend\Scripts\activate.bat`
1. `export FLASK_APP=backend/src/app.py`
1. `flask run`

#### Frontend
1. `cd frontend/`
1. `yarn start`
