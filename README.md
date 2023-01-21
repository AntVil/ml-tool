# ml-tool

[documentation](./doc/README.md)

### setup
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
