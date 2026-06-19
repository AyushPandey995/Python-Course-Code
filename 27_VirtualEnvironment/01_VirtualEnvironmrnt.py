"""A virtual environment is a self-contained directory that contains its own Python interpreter and libraries. This means that libraries installed in one virtual environment won't interfere with libraries in another."""

"""
To install Virtual Environment - 'pip install virtualenv'
To Create Virtual Environment - 'python -m venv Env1' (Env1 is the name of Virtual environment)
To activate Virtual Environment - '.\env1\Scripts\Activate.ps1'

Now we can install different packages which we have to use for this particular environment, ex - 'pip install numpy'
If the package is already available in your computer then also the python will install that package separately for this virual environment.
We can also install particular version of any package, ex- 
'pip install numpy==1.20.0'

We can see the list of packages installed for this environment using - 'pip list'

To upgrade the outdated packages - 'pip install --upgrade requests', ('requests' is the name of package)

To uninstall any package - 'pip uninstall requests'

A requirements.txt file lists all the packages your project depends on. This makes it easy to recreate the environment on another machine.
syntax - 'pip freeze > requirements.txt'
To install all the packages at once present in requirements.txt,
 - 'pip install -r requirements.txt'

 Deactivating the virtual environment- 'deactivate'

"""
