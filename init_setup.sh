echo [$(date)]: "START"

echo [$(date)]: "Creating env with Python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(date)]: "Activating the environment"

source activate ./env

echo [$(date)]: "Installing the dev requirements"

python -m pip install --upgrade pip

pip install -r requirements.txt 

echo [$(date)]: "END"