echo [$(date)]: "START"

echo [$(date)]: "Creating conda env with Python 3.9 version"

conda create -p ./env python=3.9 -y
# python -m venv .venv

echo [$(date)]: "Activating the environment"

# source .venv/Scripts/activate
# conda update conda

echo [$(pwd)]
conda activate $(pwd)/env
# source activate venv

echo [$(date)]: "Installing the dev requirements"

python -m pip install --upgrade pip

pip install -r requirements.txt 

echo [$(date)]: "Installing the project as local package"

# python setup.py install

echo [$(date)]: "END"