# ml-tool

[documentation](./doc/README.md)

### setup
Make sure you have one of the following python versions installed: `3.8`, `3.9`, `3.10`
```
python --version
```

Create a virtual environment
```
python -m venv venv
```

Activate the environment

Windows:
```
./venv/Scripts/active
```
Unix:
```zsh
source venv/bin/activate
```

To deactivate the environment later

Windows:
```
./venv/Scripts/deactivate
```
Unix:
```zsh
deactivate
```

Upgrade pip to the newest version
(venv's often don't have newest pip)
```
pip install --upgrade pip
```

Install required dependencies
```
pip install -r requirements.txt
```

*In case of errors with `psycopg2` install `psycopg2-binary` instead*

Change the constants for the database in [./src/constants.py](./src/constants.py)

Run the project
```
python src/main.py
```

Keep requirements up to date when installing new dependencies
```
pip freeze > requirements.txt
```

### testing
To test if everything is installed and running correct you can run the examples in `./examples/`
