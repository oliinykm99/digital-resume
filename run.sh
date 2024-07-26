#!/bin/zsh

# Folder that contains all locally installed packages
DIRECTORY=.venv

echo "Activating ${DIRECTORY}"
source ${DIRECTORY}/bin/activate

echo "Running main.py script"
streamlit run Mainpage.py

echo "Deactivating ${DIRECTORY}"
deactivate
