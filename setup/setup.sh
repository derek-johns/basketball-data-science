#!/usr/bin/env bash
# a bash script to setup the environment for the project

# install pip3 and virtualenv
sudo apt-get install python3-pip -y

# create the virtual environment in the project root
pip3 install virtualenv
virtualenv -p python3 basketball_data_science_env

# activate the virtual environment
source basketball_data_science_env/bin/activate

# install packages needed
pip3 install ipykernel
pip3 install jupyter
pip3 install -r ./setup/requirements.txt

# create custom kernel
python3 -m ipykernel install --user --name basketball_data_science_env --display-name "basketball-data-science-kernel"

# open jupyter notebooks
jupyter notebook