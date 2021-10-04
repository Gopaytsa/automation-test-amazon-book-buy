[Local virtual environments](#local-virtual-environments)  
[Tests run options](#tests-run-options)  
&ensp;&ensp;[Markers](#markers)  
&ensp;&ensp;[Browser](#browser)  
&ensp;&ensp;[Websites](#websites)   


## Local virtual environments
Create local environment:
```
virtualenv <venv_name>

or

path/to/python[version]/python -m venv <venv_name>
```
Activate it:  
- Windows command line  
```
<venv_name>\Scripts\activate
```
- Linux/MacOS  
```
source <venv_name>/bin/activate
```
NOTE: It is important to use virtual environment when working locally  
**IMPORTANT**: Name of your local environment should be added to .gitignore. If you work in VSCode you should also add .history and  .vscode/ to .gitignore.
  
To install dependencies in your virtual environment, use:
```
pip3 install -r requirements.txt
```

## Tests run options

Following custom options are available for executing `run.py` script:  
- `--m` (marker depending on which test is triggered or not)
- `--browser` (browser in which UI tests should be executed)

Examples:

Command fof amazon test run:
python run.py -m amazon

By default it will runs in chrome browser.

Command for parallel running in firefox browser:
python run.py --browser=firefox -m amazon

### Browser
Following browsers are supported for UI tests:
- `--browser=chrome` (by default)
- `--browser=firefox`  
