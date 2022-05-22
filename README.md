# neu-capstone
Script for parsing excel from the Capstone class

Capstone class = [ITC 6040](https://catalog.northeastern.edu/graduate/professional-studies/masters-degree-programs/informatics-mps/#programsrequirementtext) 

## Setup
### Download the code
You can either:
1. Use git cli to clone this repository
2. (If you don't know git cli) Click "Code" (green button) > Download Zip > unpack downloaded zip file in folder that you choose

### Install Jupyter Notebook
#### Terminal (requires extra dependencies)
Requires [pipenv](https://pipenv.pypa.io/en/latest/)
Use terminal:
```shell
pipenv install --python 3.8 --ignore-pipfile
pipenv shell
jupyter notebook
# to stop
CTRL + C
exit
```

#### Mac (default terminal)
1. Open terminal
2. Follow steps from https://jupyter.org/install#jupyter-notebook
3. Once Jupyter Notebook is launched navigate to the folder you downloaded the code to
4. Open notebooks > `Install pip libraries.ipynb` > follow the description

#### Windows
1. Follow this article: https://www.geeksforgeeks.org/how-to-install-jupyter-notebook-in-windows/
2. Once Jupyter Notebook is launched navigate to the folder you downloaded the code to
3. (If you used Anaconda) Open `notebooks` > `Install conda libraries.ipynb` > follow the description
4. (If you used Pip) Open `notebooks` > `Install pip libraries.ipynb` > follow the description

#### Other
There are many ways to install Jupyter Notebook and I cannot list them all.
Ensure that you do not use free cloud solutions, as they may probably 
make all uploaded survey files public.

## Usage
1. Open notebooks > Parser.ipynb > follow the description
2. Follow description
3. Get .xlsx file with parsed data in the end
