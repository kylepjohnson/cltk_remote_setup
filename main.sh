#!/bin/bash

# This was run on Ubuntu 15.04

cd
curl -O https://raw.githubusercontent.com/kylepjohnson/python3_bootstrap/master/ubuntu14.sh
chmod +x ubuntu14.sh
./ubuntu14.sh

# prereqs for gensim/scipy/numpy
apt-get install -y libblas-dev liblapack-dev
apt-get install -y python-dev gfortran

cd
pyvenv venv
source venv/bin/activate
pip install scikit-learn

pip install cltk

# at this step you must install your corpora

python import_corpora.py
