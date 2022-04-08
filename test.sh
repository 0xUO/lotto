#!/bin/bash
declare -a directories=(front-end lotto-api lottodraw-api prize-api)
for dir in "${directories[@]}"; 
do
cd ${dir}
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r test_requirements.txt 
python3 -m pytest -p no:warnings --cov=application --cov-report=html
cd ..
done