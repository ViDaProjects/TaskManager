# Configure project

1- Clone repo with git clone

2- Open it with Qt Creator using TaskManager.pyproject

3- Accept default config, then it will open project

5- Open terminal and run:

	python3 -m venv venv
	source venv/bin/activate
	pip install PySide6
	
## Generate another ui file
Run this command before run project if form.ui was updated
        
        pyside6-uic form.ui -o ui_form.py

# Run project

On terminal, use 

        python3 -m gui.mainwindow
	

