#!/bin/sh

pip install waitress==1.4.4
pip install Flask==1.1.2

pip install SQLAlchemy==1.3.23
pip install pandas==1.2.2

pip install -U scikit-learn==0.24.1


python -u main.py