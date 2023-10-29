# End to End ML Project

### Create a project folder
```bash
mkdir <"project folder name">
```

### Initialise git
```bash
git init
```

### Add file to stage
```bash
git add <"file name">
```

### Commit fils to git
```bash
git commit -m <"commit message">
```

### Push the branch to remote github
```bash
git push -u origin <"branch name">
```

### Run init_setup.sh to setup development environment
```bash
bash <'filename'>.sh
```
### Ways to install project as local package
#### 1. using setup.py
```bash
python setup.py install
```
#### 2. having '-e .' in requirement.txt 
```bash
pip install -r requirement.txt
```

![installed project as local package](image.png)



## Artifacts
Outputs of all the components:
I/P --> Raw data --> Data Ingestion --> O/P Train|Test data split
I/P --> Data Transformation --> O/P Processed data




