echo [$(date)]: "START"

echo [$(date)]: "Creating env with Python 3.8 version"

# conda create --prefix ./env python=3.8 -y
python -m venv .venv

echo [$(date)]: "Activating the environment"

source .venv/Scripts/activate

echo [$(date)]: "Installing the dev requirements"

python -m pip install --upgrade pip

pip install -r requirements.txt 

echo [$(date)]: "END"