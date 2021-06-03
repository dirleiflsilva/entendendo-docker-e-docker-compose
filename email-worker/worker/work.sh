#!/bin/bash

# instalando dependência
pip install redis==2.10.5

# subindo o worker
python -u worker.py