#! /bin/bash


cd service1/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd ..


cd service2/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd ..


