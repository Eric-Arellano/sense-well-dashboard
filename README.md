# Sense Well Dashboard
React & Flask app to visualize sensor data for clean water wells to detect when they fail prematurely.

## Prerequisites

### Install software on Mac
1. HomeBrew package manager: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
1. Git: `brew install git`
1. Python 3.6: `brew install python3`
1. Node.js & NPM: `brew install node`
1. Yarn package manager: `brew install yarn`
1. Heroku: `brew install heroku`

### Install software on PC
See [this PowerPoint](https://docs.google.com/presentation/d/1XfWRizo1ma2PfgS59i-MNBNhmjmYliMYHHhAnYY2pzM/edit#slide=id.g328c47d582_0_1431) 
for further context on how to get this project working effectively on a PC.

1. Git & Git Bash, https://git-scm.com/downloads
    1. Accept every default setting, except for choosing your default text editor:
        1. The default, Vim, is great but confusing if you've never used it.
        1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.6, https://www.python.org/downloads/ 
    1. Check on the option to add python.exe to your PATH variable.
1. Node.js & NPM, https://nodejs.org/en/ 
    1. Choose the most current version
    1. Accept default settings
1. Yarn, installer from https://yarnpkg.com/en/docs/install
1. Heroku, 64 bit installer from https://devcenter.heroku.com/articles/heroku-cli
    1. Accept defaults

## To install
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

## To simulate sending sensor data

#### Requirements
1. Make sure you can get the backend server working (see guides on 'To Install' and 'To Run')
1. [Download the app Postman](https://www.getpostman.com/)

#### Steps
1. Start the Flask backend server with `./run-backend.sh`
1. Open up the app Postman
1. Start a new "Request" and give whatever name you'd like
1. Change the method to `POST` in the top middle-left corner
1. Under `body`, change to `raw` and then on the orange text that appears to the right select `JSON (application/json)`
1. Paste the JSON values into the `body` field. You can just copy and paste [this example](https://raw.githubusercontent.com/Eric-Arellano/sense-well-dashboard/master/backend/sensor_schema.json).
1. Click `send`. 
1. At the bottom of the screen, you should get a report with the community name and daily averages. Otherwise, there 
was an error and you should check the console running the Flask server for the error message.


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
