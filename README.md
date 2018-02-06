# Sense Well Dashboard
React & Flask app to visualize sensor data for clean water wells to detect when they fail prematurely.

## Prerequisites

### Install software on Mac
1. HomeBrew package manager: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
1. Brew Cask: `brew tap caskroom/cask`
1. Git: `brew install git`
1. Python 3.6: `brew install python3`
1. Node.js & NPM: `brew install node`
1. Yarn package manager: `brew install yarn`
1. Heroku: `brew install heroku`
1. Postman: `brew cask install Postman`

### Install software on PC
See [this PowerPoint](https://docs.google.com/presentation/d/1XfWRizo1ma2PfgS59i-MNBNhmjmYliMYHHhAnYY2pzM/edit#slide=id.g328c47d582_0_1431) 
for further context on how to get this project working effectively on a PC.

1. Git & Git Bash, https://git-scm.com/downloads
    1. Accept every default setting, except for choosing your default text editor:
        1. The default, Vim, is great but confusing if you've never used it.
        1. Recommended to download the app Visual Studio Code and then choose that as your option.
1. Python 3.6, https://www.python.org/downloads/ 
    1. **Check on the option to add python.exe to your PATH variable.**
1. Node.js & NPM, https://nodejs.org/en/ 
    1. Choose the most current version
    1. Accept default settings
1. Yarn, installer from https://yarnpkg.com/en/docs/install
1. Heroku, 64 bit installer from https://devcenter.heroku.com/articles/heroku-cli#windows
    1. Accept defaults
1. Postman, https://www.getpostman.com/
    1. Accept defaults
    
### Running commands on PC
Use Git Bash instead of Command Prompt, because Git Bash offers Unix-style tools.

Due to issues with the way Python is installed on PCs, the normal command method of `./run.py` won't work. Instead,
*every time you see `./run.py`, replace it with`py run.py`*.

## Basic Usage
1. `./run.py install`, installs all the libraries
1. `./run.py`, starts the app at `localhost:3000` (go to this in your browser)
1. `./run.py stop`, stops the app

## Simulate Sensor Data
1. `./run.py --target backend` (make sure you installed the app already)
1. Open the app Postman
    1. Skip creating an account by clicking the bottom option.
1. Click "Request"
1. Provide whatever name you'd like, and add it to a whatever collection you'd like (might have to create a new collection)
1. In the top left corner, change the method from `GET` to `POST`
1. Under `body`, change to `raw`
1. From the orange dropdown to the right that says `Text`, change to `JSON (application/json)`
1. In the `body` field, paste the JSON you want.
    1. You can copy and paste [this example](https://raw.githubusercontent.com/Eric-Arellano/sense-well-dashboard/master/backend/sensor_schema.json)
1. Click `send`
1. At the bottom of the screen, you should get a report with the community name and daily averages. Otherwise, there was an error and you should check the console running the Flask server for the error message.
1. `./run.py --target backend stop`

## Advanced Usage
There are many different ways to run this application, such as only starting the backend server or only starting the frontend server.

#### Understanding the below syntax
You will encounter these symbols:
* `a|b` = a or b. You must choose one.
* `[a]` = a is optional. You can add it as an argument if you'd like, otherwise the defaults will be used. 

#### Targeting environment
Most of these commands default to running on every possible environment (scripts, backend, and frontend). 
You can often specify a specific target with `--target [env]`, or the abbreviation `-t [env]`.

### Install
`./run.py install [--target backend|frontend]`

### Run
* Start app: `./run.py [--target backend|frontend]`
* Stop app: `./run.py stop [--target backend|frontend]`

### Test
* Run unit tests: `./run.py test [--target backend|script]`
* Check types: `./run.py types [--target backend|frontend|script]`

### Deploy
`./run.py deploy`

### Dependency management
* Catchup from changes made by others: `./run.py catchup [--target backend|frontend]`
* View outdated dependencies: `./run.py outdated [--target backend|frontend]`
* View dependency tree: `./run.py deptree [--target backend]` (not supported on frontend)
* Add package(s): `./run.py add package1 [package2...] --target backend|frontend`
* Upgrade package(s): `./run.py upgrade package1 [package2...] --target backend|frontend`
* Remove package(s): `./run.py remove package1 [package2...] --target backend|frontend`
